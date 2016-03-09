def application(environ, start_response):
    resp = environ['QUERY_STRING'].split("&")
    resp = [item+"\r\n" for item in resp]
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return resp
