def application(environ, start_response):
    start_response('200 ok', [('Content-Type', 'text/html')])
    print environ
    return '<h1>Hello,WGSI!</h1>'
