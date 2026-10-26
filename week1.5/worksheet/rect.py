class Rectangle:
    """A rectangle defined by its width and height."""

    def __init__(self, width: int, height: int):
        """Initialize a Rectangle with the given width and height.

        Args:
            width: The width of the rectangle (must be a positive int).
            height: The height of the rectangle (must be a positive int).

        Raises:
            TypeError: If width or height is not an int.
            ValueError: If width or height is less than or equal to 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an int")
        if not isinstance(height, int):
            raise TypeError("height must be an int")
        if width <= 0:
            raise ValueError("width must be greater than 0")
        if height <= 0:
            raise ValueError("height must be greater than 0")
        self.width = width
        self.height = height

    def is_square(self) -> bool:
        """Return True if the rectangle is a square, False otherwise."""
        return self.width == self.height

    def area(self) -> int:
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> int:
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
