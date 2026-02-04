#!/usr/bin/python3
"""Module that defines a Square class.

This module provides a Square class that inherits from Rectangle
with a private size attribute validated as a positive integer.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle.

    This class represents a square with a private size attribute
    that is validated as a positive integer.
    """

    def __init__(self, size):
        """Initialize a Square with validated size.

        Args:
            size (int): Positive integer representing the square's side length.

        Raises:
            TypeError: When size is not an integer.
            ValueError: When size is not greater than 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
