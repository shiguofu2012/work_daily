#!/usr/bin/python
from wsgiref.simple_server import make_server
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class application:
    def __init__(self, env, start_response):
        print env

    def __iter__(self):
        yield 'hello world'


def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Hello World", "Hello wsgi"]


httpd = make_server('', 8000, app)
print "serving on port 8000..."
import webbrowser
#webbrowser.open('http://localhost:8000')
httpd.handle_request()
