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
