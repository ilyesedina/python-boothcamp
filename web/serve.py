"""Serve the browser playground locally.

Run from anywhere:  python web/serve.py   (then open http://localhost:8000)

The extra headers enable SharedArrayBuffer, which lets Python's input()
pause and wait for you to type in the browser.
"""
import functools
import http.server
import os
import platform
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
# Inside WSL, listen on all interfaces so the Windows browser can reach it.
# (WSL's network is private to this PC.) Elsewhere, stay on this machine only.
HOST = "0.0.0.0" if "microsoft" in platform.release().lower() else "127.0.0.1"


class Handler(http.server.SimpleHTTPRequestHandler):
    # Windows can map .js to text/plain via the registry, which browsers refuse
    # to run as a module, so set the important types explicitly.
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".js": "text/javascript",
        ".mjs": "text/javascript",
        ".css": "text/css",
        ".html": "text/html",
        ".py": "text/plain; charset=utf-8",
        ".wasm": "application/wasm",
    }

    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


if __name__ == "__main__":
    handler = functools.partial(Handler, directory=ROOT)
    with http.server.ThreadingHTTPServer((HOST, PORT), handler) as server:
        print(f"Python Bootcamp playground: http://localhost:{PORT}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
