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

        "color": "#565287",
        "secondary_color": "#7d7989",
        "head_url": "http://orig10.deviantart.net/cf94/f/2012/317/1/6/snake_wallpaper__by_shadow_of_nemo-d5kwelc.jpg",
        "name": "Shadow Snek",
        "head_type": "smile",
        "tail_type": "curled"
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
        # 'up', 'down', 'left', 'right'
        'move': selection,
        'taunt': 'Come at me!'
    }


run(host='0.0.0.0', port=8080)
