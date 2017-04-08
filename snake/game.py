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

    def add_food(self, food_state):
        self.food = [list(food_coord) for food_coord in food_state]

    def has_food(self, pos):
        """Checks whether food is at an (x, y) coordinate"""
        for coord in self.food:
            if coord == pos:
                return True
        return False

    def has_snake(self, coord):
        """Checks whether a snake is at the (x, y) position"""
        for snake_id in self.snakes.keys():
            snake = self.snakes[snake_id]
            for snake_coord in snake.coords:
                if snake_coord == coord:
                    return True
        return False

    def is_off_board(self, coord):
        return coord[0] >= self.width or coord[1] >= self.height or -1 in coord

    def is_safe(self, coord):
        """Check if the coordinate is not populated by a snake"""
        return not self.has_snake(coord) and not self.is_off_board(coord)

    def coord_for_direction(self, direction):
        """Get an (x, y) coordinate for a direction"""
        current_coord = self.current_head[:]
        if direction == 'up':
            current_coord[1] -= 1  # huh?
        elif direction == 'down':
            current_coord[1] += 1
        elif direction == 'left':
            current_coord[0] -= 1
        elif direction == 'right':
            current_coord[0] += 1
        return current_coord

    def is_safe_move(self, direction):
        """Check if the direction is safe"""
        return self.is_safe(self.coord_for_direction(direction))

    def update_state(self, new_state):
        """Called with the server state"""
        self.snake_id = new_state['you']
        for new_snake_state in new_state['snakes']:
            self.add_snake(new_snake_state)
        self.add_food(new_state['food'])
        self.remove_dead_snakes(new_state['dead_snakes'])
