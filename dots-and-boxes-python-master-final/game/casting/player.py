from game.casting.actor import Actor

class Player(Actor):
    """Creates an individual player object"""
    def __init__(self, player_name):
        super().__init__()
        self._points = 0
        self._text = player_name

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points

    def get_points(self):
        """Returns an int with the current point value"""
        return self._points