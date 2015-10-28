#!/usr/bin/env python3
"""
Run the server in a production environment
"""
from api import app, api_init
from aiohttp_wsgi import serve

app.config.from_object('config')

api_init()

addr = {
    'host': '0.0.0.0',
    'port': 8080
}
print("Starting server on {host}:{port}".format(**addr))
serve(app, **addr)

