#!/usr/bin/env python3
"""Thin HTTP shell over allin_anything.webapp.DemoApp (logic lives in src, never here).

Usage: python3 scripts/webapp.py [port]   (default 8642; serves webapp/index.html + /api/*)
"""

from __future__ import annotations

import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from allin_anything.webapp import DemoApp  # noqa: E402

APP = DemoApp(ROOT)
INDEX = ROOT / "webapp" / "index.html"


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj: object, code: int = 200) -> None:
        self._send(code, json.dumps(obj).encode(), "application/json; charset=utf-8")

    def do_GET(self) -> None:  # noqa: N802 (http.server API)
        if self.path in ("/", "/index.html"):
            self._send(200, INDEX.read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/api/registry":
            self._json(APP.registry_summary())
        elif self.path == "/api/chains":
            self._json(APP.chain_list())
        elif self.path == "/api/penecho":
            self._json(APP.penecho_bridge())
        elif self.path == "/manifest.json":
            self._send(200, (ROOT / "webapp" / "manifest.json").read_bytes(),
                       "application/manifest+json")
        elif self.path == "/bitter-lesson":
            self._send(200, (ROOT / "examples" / "bitter-lesson" / "index.html").read_bytes(),
                       "text/html; charset=utf-8")
        elif self.path == "/assets/penecho-two-curves.png":
            self._send(200, (ROOT / "examples" / "bitter-lesson" / "assets" / "penecho-two-curves.png").read_bytes(),
                       "image/png")
        else:
            self._json({"error": "not found"}, 404)

    def do_POST(self) -> None:  # noqa: N802
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0)) or 0) or b"{}")
        except Exception:
            return self._json({"error": "send JSON"}, 400)
        if self.path == "/api/route":
            self._json(APP.route(str(body.get("intent", ""))))
        elif self.path == "/api/autorun":
            self._json(APP.autorun(str(body.get("chain", ""))))
        else:
            self._json({"error": "not found"}, 404)

    def log_message(self, fmt: str, *args: object) -> None:
        pass  # keep the demo console clean


def main() -> int:
    """Serve the demo on localhost only (this is a local demo, not a deployment).

    1-click activation (playbook rule): starting the server IS the demo — the browser
    opens itself unless --no-open is passed (CI/headless).
    """
    args = [a for a in sys.argv[1:] if a != "--no-open"]
    port = int(args[0]) if args else 8642
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{port}"
    print(f"✓ allin-anything demo → {url}  (Ctrl-C stops)")
    if "--no-open" not in sys.argv:
        import threading
        import webbrowser

        threading.Timer(0.4, webbrowser.open, args=(url,)).start()
    server.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
