// Runs Python (Pyodide) off the main thread so input() can block while
// waiting for the user to type, exactly like a real terminal.
const PYODIDE_URL = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/";
importScripts(PYODIDE_URL + "pyodide.js");

const SETUP = String.raw`
import builtins, importlib, os, runpy, sys, traceback, warnings, js

# ASCII art with backslashes triggers noisy SyntaxWarnings; hide them.
warnings.filterwarnings("ignore", category=SyntaxWarning)

ROOT = "/home/pyodide/projects"

def _input(prompt=""):
    sys.stdout.write(str(prompt))
    sys.stdout.flush()
    sys.stderr.flush()
    return js.readLine()

builtins.input = _input
builtins.exit = builtins.quit = sys.exit
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(line_buffering=True)
    except Exception:
        pass

def run_project(folder, script):
    # Forget modules from a previous run (several days have their own art.py).
    for name, mod in list(sys.modules.items()):
        if (getattr(mod, "__file__", None) or "").startswith(ROOT):
            del sys.modules[name]
    path = f"{ROOT}/{folder}"
    sys.path[:] = [p for p in sys.path if not p.startswith(ROOT)]
    sys.path.insert(0, path)
    os.chdir(path)
    importlib.invalidate_caches()
    try:
        runpy.run_path(f"{path}/{script}", run_name="__main__")
    except SystemExit as e:
        if isinstance(e.code, str):
            print(e.code, file=sys.stderr)
        elif e.code not in (None, 0):
            print(f"Exited with code {e.code}", file=sys.stderr)
    except BaseException as e:
        tb = e.__traceback__
        while tb is not None and not tb.tb_frame.f_code.co_filename.startswith(ROOT):
            tb = tb.tb_next
        traceback.print_exception(type(e), e, tb)
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
`;

let pyodide, ctl, buf, runProject;

// Called from Python's input(): ask the page for a line, then sleep until it arrives.
self.readLine = () => {
  postMessage({ type: "input" });
  Atomics.wait(ctl, 0, 0);
  const length = Atomics.load(ctl, 1);
  const text = new TextDecoder().decode(buf.slice(0, length));
  Atomics.store(ctl, 0, 0);
  return text;
};

function streamTo(type) {
  const decoder = new TextDecoder();
  return {
    write(bytes) {
      postMessage({ type, text: decoder.decode(bytes, { stream: true }) });
      return bytes.length;
    },
  };
}

self.onmessage = async ({ data }) => {
  if (data.type === "init") {
    ctl = new Int32Array(data.sab, 0, 2);
    buf = new Uint8Array(data.sab, 8);
    try {
      pyodide = await loadPyodide({ indexURL: PYODIDE_URL });
      pyodide.setStdout(streamTo("out"));
      pyodide.setStderr(streamTo("err"));
      pyodide.setStdin({ stdin: () => self.readLine() });
      pyodide.runPython(SETUP);
      runProject = pyodide.globals.get("run_project");
      postMessage({ type: "ready", version: pyodide.version });
    } catch (err) {
      postMessage({ type: "fatal", message: String(err) });
    }
  } else if (data.type === "run") {
    const dir = `/home/pyodide/projects/${data.folder}`;
    pyodide.FS.mkdirTree(dir);
    for (const [name, text] of Object.entries(data.files)) {
      pyodide.FS.writeFile(`${dir}/${name}`, text);
    }
    try {
      runProject(data.folder, data.script);
    } catch (err) {
      postMessage({ type: "err", text: String(err) + "\n" });
    }
    postMessage({ type: "done" });
  }
};
