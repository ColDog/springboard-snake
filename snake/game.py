from .snake import Snake


class Game:

    def __init__(self, game_id, snake_id, width, height):
        self.game_id = game_id
        self.width = width
        self.height = height
        self.snake_id = snake_id
        self.snakes = {}
        self.dead_snakes = {}
        self.food = []

    @property
    def me(self):
        return self.snakes[self.snake_id]

    @property
    def current_head(self):
        return self.me.current_head

    def add_food(self, food_state):
        self.food = [list(food_coord) for food_coord in food_state]

    def add_snake(self, snake_state):
        """Add's a snake"""
        snake = self.snakes.get(snake_state['id'])
        if snake is None:
            snake = Snake(
                snake_id=snake_state['id'],
                name=snake_state['name'],
                hp=snake_state['health_points'],
            )
            self.snakes[snake.snake_id] = snake
        snake.set_coords(snake_state['coords'])

    def remove_dead_snakes(self, dead_snake_state):
        for dead_snake in dead_snake_state:
            if self.snakes[dead_snake['id']]:
                self.dead_snakes = self.snakes[dead_snake['id']]
                del self.snakes[dead_snake['id']]

    def update_state(self, new_state):
        """Called with the server state"""
        self.snake_id = new_state['you']
        for new_snake_state in new_state['snakes']:
            self.add_snake(new_snake_state)
        self.add_food(new_state['food'])
        self.remove_dead_snakes(new_state['dead_snakes'])
