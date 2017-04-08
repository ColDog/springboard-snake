import random
from .helpers import Helpers


class Runner(Helpers):

    directions = ['up', 'down', 'left', 'right']

    def __init__(self, game):
        super().__init__(game)
        self.game = game

    def move(self):
        while True:
            # select a random direction
            selection = random.choice(self.directions)
            if self.is_safe_move(selection):
                return selection
