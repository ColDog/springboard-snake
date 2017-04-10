import random
import math
from .helpers import Helpers


class Runner(Helpers):

    directions = ['up', 'down', 'left', 'right']

    def __init__(self, game):
        super().__init__(game)
        self.game = game

    def move_towards(self, coord):
        """Points the snake in the direction of the coordinate"""
        head = self.game.current_head
        # move up / down, then left right
        if head[1] == coord[1]:
            # move left right
            if head[0] == coord[0]:
                return None  # we are there!
            elif head[0] < coord[0]:
                return 'right'
            elif head[0] > coord[0]:
                return 'left'
        elif head[1] < coord[1]:
            return 'down'
        elif head[1] > coord[1]:
            return 'up'

    def is_a_safe_move(self, direction):
        snake_parts = self.snake_parts()
        anticipated_coords = self.coord_for_direction(direction)
        if -1 in anticipated_coords or 21 in anticipated_coords:
            return False
        for snake_part in snake_parts:
            if snake_part == anticipated_coords:
                return False
        return True

    def move_x(self, x_diff):
        if x_diff <= 0:
            return 'left'
        else:
            return 'right'

    def move_y(self, y_diff):
        if y_diff <= 0:
            return 'up'
        else:
            return 'down'

    def nearest_food(self):
        if self.game.food_direction not in self.game.food:
            self.game.food_direction = None

        if self.game.food_direction:
            return self.game.food_direction
        min_val = 1000
        min_idx = 0
        for idx, food_coord in enumerate(self.game.food):
            distance = distance_of_points(self.game.current_head, food_coord)
            if distance < min_val:
                min_val = distance
                min_idx = idx
        self.game.food_direction = self.game.food[min_idx]
        return self.game.food_direction

    def move_snake(self, head_coord, food_coord):
        """head_coord (x, y), food_coord (x, y)"""
        x_diff = food_coord[0] - head_coord[0] # -6
        y_diff = food_coord[1] - head_coord[1] # 12
        print(x_diff, y_diff)

        if abs(x_diff) > abs(y_diff):
            return self.move_x(x_diff)
        else:
            return self.move_y(y_diff)

    def move(self):
        # select a random direction
        # food = self.game.food[0]
        food = self.nearest_food()
        # selection = self.move_snake(self.game.current_head, food)
        print(food, self.game.food)
        selection = self.move_towards(food)
        if self.is_safe_move(selection):
            return selection

        random.shuffle(self.directions)
        safe_directions = [direction for direction in self.directions if self.is_safe_move(direction)]
        print('safe', safe_directions)
        return safe_directions[0]


def distance_of_points(coord1, coord2):
    return math.sqrt(abs(math.pow(coord1[0] + coord2[0], 2) - math.pow(coord1[1] + coord2[1], 2)))
