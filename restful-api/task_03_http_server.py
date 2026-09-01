#!/usr/bin/python3
"""Provide a simple JSON and text API using ``http.server``."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle GET requests for the simple API endpoints."""

    def send_content(self, status_code, content, content_type="text/plain"):
        """Send an HTTP response with the supplied content."""
        body = content.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        """Route GET requests to supported endpoints."""
        if self.path == "/":
            self.send_content(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_content(200, json.dumps(data), "application/json")
        elif self.path == "/status":
            self.send_content(200, "OK")
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.send_content(200, json.dumps(info), "application/json")
        else:
            self.send_content(404, "Endpoint not found")


def run(port=8000):
    """Start the HTTP server on the requested port."""
    server = HTTPServer(("", port), SimpleAPIHandler)
    print("Server running on port {}".format(port))
    server.serve_forever()


if __name__ == "__main__":
    run()
