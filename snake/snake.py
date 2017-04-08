
class Snake:

    def __init__(self, snake_id=None, name=None, hp=None, coords=None):
        self.snake_id = snake_id
        self.name = name
        self.coords = coords
        self.hp = hp

    def set_coords(self, coords):
        self.coords = [list(coord) for coord in coords]

    @property
    def current_head(self):
        return self.coords[0]
