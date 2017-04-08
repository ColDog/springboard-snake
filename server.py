from bottle import route, run, request
from snake.game import Game
from snake.runner import Runner


games = {}


@route('/start', method='POST')
def start():
    data = request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    print('start', data)

    games[game_id] = Game(game_id=game_id, width=board_width, height=board_height, snake_id=None)

    return {
        "color": "#FF0000",
        "secondary_color": "#00FF00",
        "head_url": "http://placecage.com/c/100/100",
        "name": "Cage Snake",
        "head_type": "pixel",
        "tail_type": "pixel"
    }


@route('/move', method='POST')
def move():
    data = request.json
    game = games[data['game_id']]

    game.update_state(data)

    runner = Runner(game)
    selection = runner.move()

    print('move', data)
    print('moving', selection)

    return {
        'move': selection,
        'taunt': 'battlesnake-python!'
    }


run(host='0.0.0.0', port=8080)
