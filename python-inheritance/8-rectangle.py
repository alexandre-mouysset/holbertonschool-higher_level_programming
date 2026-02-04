#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry.

    This class represents a rectangle with width and height attributes.
    It validates that both dimensions are positive integers.

    Attributes:
        __width (int): The private width attribute of the rectangle.
        __height (int): The private height attribute of the rectangle.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height.

        Args:
            width (int): The width of the rectangle > 0
            height (int): The height of the rectangle > 0

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
