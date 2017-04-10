
class Helpers:

    def __init__(self, game):
        self.game = game

    def has_food(self, pos):
        """Checks whether food is at an (x, y) coordinate"""
        for coord in self.game.food:
            if coord == pos:
                return True
        return False

    def snake_parts(self):
        snake_parts = []
        for snake_id in self.game.snakes.keys():
            snake = self.game.snakes[snake_id]
            for snake_coord in snake.coords:
                snake_parts.append(snake_coord)
        return snake_parts

    def has_snake(self, coord):
        """Checks whether a snake is at the (x, y) position"""
        for snake_id in self.game.snakes.keys():
            snake = self.game.snakes[snake_id]
            for snake_coord in snake.coords:
                if snake_coord == coord:
                    return True
        return False

    def is_off_board(self, coord):
        return coord[0] >= self.game.width or coord[1] >= self.game.height or -1 in coord

    def is_safe(self, coord):
        """Check if the coordinate is not populated by a snake"""
        return not self.has_snake(coord) and not self.is_off_board(coord)

    def coord_for_direction(self, direction):
        """Get an (x, y) coordinate for a direction"""
        current_coord = self.game.current_head[:]
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
