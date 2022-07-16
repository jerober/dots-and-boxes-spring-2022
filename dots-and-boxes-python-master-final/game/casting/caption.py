from game.casting.actor import Actor

class Caption(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _player_text (str): The initial caption for the game
    """
    def __init__(self, start_caption):
        super().__init__()
        self._text = start_caption

    def set_caption(self, caption_text):
        """Sets the display caption
        
        Args:
            caption_text (str): Indicates the game status to be displayed.
        """
        self._text = caption_text

    def get_caption(self):
        """Returns display caption"""
        return self._text
