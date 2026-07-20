#!/usr/bin/env python3
"""Serve the evaluation GUI and write its records straight into ``evaluations/``.

A browser opened from ``file://`` cannot write to disk without a save dialog per
record, which makes rating a batch of runs tedious enough that it stops
happening. This is the smallest thing that removes that friction: a localhost
static server plus one POST endpoint.

    python serve_evaluations.py            # serve and open the GUI
    python serve_evaluations.py --port 8123 --no-browser

Bound to 127.0.0.1 only. Writes nothing outside ``evaluations/``, accepts only
``.json`` filenames with no path separators, and never overwrites an existing
record — a second evaluation of the same run by the same rater is kept as
``__2``, because rater disagreement over time is data rather than a conflict.
"""

import argparse
import http.server
import json
import os
import re
import socketserver
import threading
import webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
EVAL_DIR = os.path.join(HERE, "evaluations")
GUI = "evaluate_results_gui.html"
SAFE_NAME = re.compile(r"^[A-Za-z0-9._-]+\.json$")


def unique_path(directory, filename):
    """Return a path that does not exist yet, suffixing __2, __3, ... as needed."""
    stem, ext = os.path.splitext(filename)
    candidate = os.path.join(directory, filename)
    counter = 2
    while os.path.exists(candidate):
        candidate = os.path.join(directory, "{}__{}{}".format(stem, counter, ext))
        counter += 1
    return candidate


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=HERE, **kwargs)

    def log_message(self, fmt, *args):
        if self.path.startswith("/api/"):
            super().log_message(fmt, *args)

    def _json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.rstrip("/") == "/api/ping":
            return self._json(200, {"service": "find-sota-papers-eval", "version": 1})
        return super().do_GET()

    def do_POST(self):
        if self.path.rstrip("/") != "/api/save":
            return self._json(404, {"error": "unknown endpoint"})

        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            return self._json(400, {"error": "bad Content-Length"})
        if length <= 0 or length > 8 * 1024 * 1024:
            return self._json(400, {"error": "empty or oversized body"})

        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, ValueError) as exc:
            return self._json(400, {"error": "invalid JSON: {}".format(exc)})

        filename = payload.get("filename")
        record = payload.get("record")
        if not isinstance(filename, str) or not SAFE_NAME.match(filename):
            return self._json(400, {"error": "filename must be a plain *.json name"})
        if not isinstance(record, dict) or record.get("schema") != "find-sota-papers/eval@1":
            return self._json(400, {"error": "record is not find-sota-papers/eval@1"})

        os.makedirs(EVAL_DIR, exist_ok=True)
        path = unique_path(EVAL_DIR, filename)
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(record, handle, indent=2)
            handle.write("\n")

        relative = os.path.relpath(path, HERE).replace(os.sep, "/")
        print("    saved {}".format(relative))
        return self._json(200, {"path": relative})


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    parser = argparse.ArgumentParser(description="Serve the find-sota-papers evaluation GUI.")
    parser.add_argument("--port", type=int, default=8777, help="Port to listen on (default: 8777).")
    parser.add_argument("--no-browser", action="store_true", help="Do not open a browser.")
    args = parser.parse_args()

    os.makedirs(EVAL_DIR, exist_ok=True)
    url = "http://127.0.0.1:{}/{}".format(args.port, GUI)

    with Server(("127.0.0.1", args.port), Handler) as httpd:
        print("Evaluation GUI: {}".format(url))
        print("Records go to:  {}".format(os.path.relpath(EVAL_DIR, HERE)))
        print("Ctrl-C to stop.\n")
        if not args.no_browser:
            threading.Timer(0.5, webbrowser.open, args=(url,)).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
