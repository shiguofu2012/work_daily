#!/usr/bin/python
from wsgiref.simple_server import make_server
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

URL_PATTERN = (
        ('/hi', 'say_hi'),
        ('/hello', 'say_hello')
        )


class application:
    def __init__(self, env, start_response):
        print env

    def __iter__(self):
        yield 'hello world'


def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Hello World", "Hello wsgi"]


def say_hi(evn, start_response):
    start_response('200 OK', [('content-type', 'text/plain')])
    return ['hello world']


def say_hello(env, start_response):
    start_response('200 OK', [('content-type', 'text/plain')])
    return ['hi world']


class appClass:
    def _match(self, path):
        path = path.split('/')[1]
        for url, app in URL_PATTERN:
            if path in url:
                return app

    def __call__(self, env, start_response):
        path = env.get('PATH_INFO', '/')
        app = self._match(path)
        print path, app
        if app:
            app = globals()[app]
            return app(env, start_response)
        else:
            start_response('404 NOT FOUND', [('Content-type', 'text/plain')])
            return ['Page does not exists']
httpd = make_server('', 8000, appClass())
print "serving on port 8000..."
import webbrowser
#webbrowser.open('http://localhost:8000')
while True:
    httpd.handle_request()
