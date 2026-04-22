#!/usr/bin/env python3
"""Inicia o portal local e abre no navegador automaticamente."""

import http.server
import socketserver
import threading
import webbrowser
from pathlib import Path

PORT = 8000
DIRECTORY = Path(__file__).resolve().parent / "public"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}"
    print(f"Portal Areia Ana iniciado em: {url}")
    print("Pressione Ctrl + C para encerrar.")

    threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    httpd.serve_forever()
