#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'a test module'
__author__ = 'nyc'

# def application(environ,start_response):
#     start_response('200 OK',[('Content-Type','text/html')])
#     return  [b'<h1>hello web!</h1>']


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]