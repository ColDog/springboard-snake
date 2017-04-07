from bottle import route, run, request


@route('/start', method='POST')
def start():
    return {'ok': True}


@route('/move', method='POST')
def move():
    body = request.json
    return {}


run(host='localhost', port=8080)
