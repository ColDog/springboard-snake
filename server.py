from bottle import route, run, request
import random
from snake.game import Game

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

    directions = ['up', 'down', 'left', 'right']

    while 1:
        selection = random.choice(directions)
        if game.is_safe_move(selection):
            break

    print('move', data['snakes'][0]['coords'], selection, game.current_head, game.coord_for_direction(selection))

    return {
        'move': selection,
        'taunt': 'battlesnake-python!'
    }


run(host='0.0.0.0', port=8080)
