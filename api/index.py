# api/index.py

from app import app as flask_app

def handler(environ, start_response):
    return flask_app(environ, start_response)
