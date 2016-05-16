def wsgi_application(environ, start_response):

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    query = environ['QUERY_STRING'].split('&')
    body = ''
    for param in query:
        body += param + '\n'
    print body
    
    start_response(status, headers)
    return body
