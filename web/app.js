import { PROJECTS } from "./projects.js";

const SCRIPT = "main.py";
const $ = (id) => document.getElementById(id);
const el = {
  days: $("day-list"),
  day: $("project-day"),
  title: $("project-title"),
  path: $("project-path"),
  consoleName: $("console-name"),
  console: document.querySelector(".console"),
  terminal: $("terminal"),
  run: $("run-btn"),
  stop: $("stop-btn"),
  clear: $("clear-btn"),
  form: $("input-form"),
  stdin: $("stdin"),
  send: $("send-btn"),
  status: $("status"),
  source: $("source"),
  sourceName: $("source-name"),
  sourceCode: $("source-code"),
  banner: $("banner"),
};

let worker = null;
let ctl = null; // Int32Array [hasInput, length] shared with the worker
let inbox = null; // Uint8Array holding the typed line
let state = "loading";
let current = null;
let runWhenReady = false;

const dayNumber = (p) => Number(p.folder.replace(/\D/g, ""));
const available = PROJECTS.filter((p) => p.main !== false);

/* ---------- Terminal output ---------- */
function write(text, kind = "out") {
  const last = el.terminal.lastElementChild;
  if (last && last.dataset.kind === kind) {
    last.textContent += text;
  } else {
    const span = document.createElement("span");
    span.dataset.kind = kind;
    span.className = kind;
    span.textContent = text;
    el.terminal.append(span);
  }
  el.terminal.scrollTop = el.terminal.scrollHeight;
}

function clearTerminal() {
  el.terminal.textContent = "";
}

/* ---------- Status ---------- */
const LABELS = {
  loading: "Loading Python…",
  ready: "Ready",
  running: "Running",
  input: "Waiting for your input",
  error: "Python unavailable",
};

function setState(next) {
  state = next;
  el.status.dataset.state = next;
  el.status.textContent = LABELS[next];
  const busy = next === "running" || next === "input";
  el.run.disabled = next === "error" || !current;
  el.run.textContent = busy ? "↻ Restart" : "▶ Run";
  el.stop.disabled = !busy;
  el.stdin.disabled = next !== "input";
  el.send.disabled = next !== "input";
  el.console.classList.toggle("waiting", next === "input");
  el.stdin.placeholder = next === "input" ? "Type your answer, then Enter" : "Press Run to start";
  if (next === "input") el.stdin.focus();
}

function showBanner(html) {
  el.banner.innerHTML = html;
  el.banner.hidden = false;
}

/* ---------- Python worker ---------- */
function startWorker() {
  const sab = new SharedArrayBuffer(8 + 16384);
  ctl = new Int32Array(sab, 0, 2);
  inbox = new Uint8Array(sab, 8);
  worker = new Worker("web/py-worker.js");
  worker.onmessage = onWorkerMessage;
  worker.onerror = (e) => {
    setState("error");
    write(`\nCould not start Python: ${e.message || "network error"}\n`, "err");
  };
  worker.postMessage({ type: "init", sab });
  setState("loading");
}

function onWorkerMessage({ data }) {
  switch (data.type) {
    case "ready":
      setState("ready");
      if (runWhenReady) {
        runWhenReady = false;
        run();
      }
      break;
    case "out":
      write(data.text, "out");
      break;
    case "err":
      write(data.text, "err");
      break;
    case "input":
      setState("input");
      break;
    case "done":
      write("\n— program finished —\n", "sys");
      setState("ready");
      break;
    case "fatal":
      setState("error");
      write(`\nPython failed to load: ${data.message}\n`, "err");
      break;
  }
}

function restartWorker() {
  worker?.terminate();
  startWorker();
}

/* ---------- Loading project files ---------- */
async function fetchText(path) {
  const res = await fetch(path, { cache: "no-cache" });
  if (!res.ok) throw new Error(`${path} (${res.status})`);
  return res.text();
}

async function loadFiles(project) {
  const names = [SCRIPT, ...(project.imports || [])];
  const texts = await Promise.all(names.map((n) => fetchText(`${project.folder}/${n}`)));
  return Object.fromEntries(names.map((n, i) => [n, texts[i]]));
}

/* ---------- Running ---------- */
async function run() {
  if (!current) return;
  if (state === "running" || state === "input") {
    write("\n— restarting —\n", "sys");
    runWhenReady = true;
    restartWorker();
    return;
  }
  if (state === "loading") {
    runWhenReady = true;
    return;
  }
  const project = current;
  let files;
  try {
    files = await loadFiles(project);
  } catch (err) {
    write(`Could not load ${err.message}\n`, "err");
    return;
  }
  clearTerminal();
  write(`$ python ${project.folder}/${SCRIPT}\n\n`, "sys");
  setState("running");
  worker.postMessage({ type: "run", folder: project.folder, script: SCRIPT, files });
}

function stop() {
  if (state !== "running" && state !== "input") return;
  write("\n— stopped —\n", "sys");
  restartWorker();
}

el.form.addEventListener("submit", (e) => {
  e.preventDefault();
  if (state !== "input") return;
  const value = el.stdin.value;
  el.stdin.value = "";
  write(value + "\n", "in");
  const bytes = new TextEncoder().encode(value).slice(0, inbox.length);
  inbox.set(bytes);
  Atomics.store(ctl, 1, bytes.length);
  Atomics.store(ctl, 0, 1);
  Atomics.notify(ctl, 0);
  setState("running");
});

el.run.addEventListener("click", run);
el.stop.addEventListener("click", stop);
el.clear.addEventListener("click", clearTerminal);
el.terminal.addEventListener("click", () => {
  if (state === "input" && !window.getSelection().toString()) el.stdin.focus();
});

/* ---------- Day navigation ---------- */
function renderNav() {
  el.days.innerHTML = "";
  for (const project of PROJECTS) {
    const li = document.createElement("li");
    const link = document.createElement("a");
    link.className = "day-link" + (project.main === false ? " missing" : "");
    link.href = `#${project.folder}`;
    link.dataset.folder = project.folder;
    link.title = `Day ${dayNumber(project)}: ${project.title}`;
    link.innerHTML = `<span class="num"></span><span class="name"></span>`;
    link.querySelector(".num").textContent = String(dayNumber(project)).padStart(2, "0");
    link.querySelector(".name").textContent = project.title;
    li.append(link);
    el.days.append(li);
  }
}

async function selectFromHash() {
  const folder = location.hash.slice(1);
  const project = PROJECTS.find((p) => p.folder === folder) || available[0];
  if (project === current) return;

  if (state === "running" || state === "input") restartWorker();
  current = project;

  for (const link of el.days.querySelectorAll(".day-link")) {
    if (link.dataset.folder === project.folder) {
      link.setAttribute("aria-current", "page");
      link.scrollIntoView({ block: "nearest", inline: "nearest" });
    } else {
      link.removeAttribute("aria-current");
    }
  }

  el.day.textContent = `Day ${dayNumber(project)}`;
  el.title.textContent = project.title;
  el.path.textContent = `${project.folder}/${SCRIPT}`;
  el.consoleName.textContent = `${project.folder}/${SCRIPT}`;
  el.sourceName.textContent = `${project.folder}/${SCRIPT}`;
  clearTerminal();

  if (project.main === false) {
    current = null;
    el.source.hidden = true;
    write(`${project.folder} has no ${SCRIPT} yet, so there is nothing to run for this day.\n`, "sys");
    setState(state);
    return;
  }

  el.source.hidden = false;
  write(`Press ▶ Run to start ${project.title}.\n`, "sys");
  setState(state);
  el.sourceCode.textContent = "Loading…";
  try {
    el.sourceCode.textContent = await fetchText(`${project.folder}/${SCRIPT}`);
  } catch (err) {
    el.sourceCode.textContent = `Could not load ${err.message}`;
  }
}

window.addEventListener("hashchange", selectFromHash);

/* ---------- Startup ---------- */
async function ensureIsolation() {
  if (window.crossOriginIsolated) {
    try { sessionStorage.removeItem("coi-reloaded"); } catch {}
    return true;
  }
  if (location.protocol === "file:") {
    showBanner(
      "This page can't run Python when opened as a file. Start the local server with " +
        "<code>python web/serve.py</code> and open <code>http://localhost:8000</code>."
    );
    return false;
  }
  if ("serviceWorker" in navigator) {
    let alreadyTried = false;
    try { alreadyTried = sessionStorage.getItem("coi-reloaded") === "1"; } catch {}
    if (!alreadyTried) {
      try {
        await navigator.serviceWorker.register("coi-sw.js");
        await navigator.serviceWorker.ready;
        try { sessionStorage.setItem("coi-reloaded", "1"); } catch {}
        location.reload();
        return false;
      } catch {}
    }
  }
  showBanner(
    "Your browser blocked the feature Python needs to wait for input (SharedArrayBuffer). " +
      "Run <code>python web/serve.py</code> and open <code>http://localhost:8000</code>."
  );
  return false;
}

document.body.dataset.appStarted = "1";
renderNav();
selectFromHash();
if (await ensureIsolation()) {
  startWorker();
} else {
  setState("error");
}
