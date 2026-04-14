#!/usr/bin/env python3
"""Simple HTTP server for the Dunkin' Donuts Remote Work Locator"""

import http.server
import socketserver
import os
import sys

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header(
            'Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Expires', '0')
        super().end_headers()


try:
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🍩 Dunkin' Donuts Remote Work Locator")
        print(f"Server running at http://localhost:{PORT}")
        print(f"👉 Open http://localhost:{PORT} in your browser")
        print(f"\nPress Ctrl+C to stop the server\n")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\n👋 Server stopped")
    sys.exit(0)
except OSError as e:
    if e.errno == 48:  # Port already in use
        print(f"❌ Port {PORT} is already in use")
        print(f"Try a different port: python3 server.py 8001")
    else:
        print(f"❌ Error: {e}")
    sys.exit(1)
