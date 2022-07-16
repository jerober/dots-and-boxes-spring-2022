class Actor():
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _image (arg:path): The image that is displayed
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._text = ""
        self._image = ""

    def get_image(self):
        """Gets the actor's image.
        
        Returns:
            Path: The actor's image.
        """
        return self._image

    def get_text(self):
        """Gets the actor's text.
        
        Returns:
            string: The actor's text.
        """
        return self._text

    def set_image(self, image):
        """Updates the image to the given one.
        
        Args:
            image (string): The given image.
        """
        self._image = image

    def set_text(self, text):
        """Updates the text to the given one.
        
        Args:
            text (string): The given text.
        """
        self._text = text