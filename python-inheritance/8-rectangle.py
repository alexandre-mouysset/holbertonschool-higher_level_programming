#!/usr/bin/python3
"""Module that defines a Rectangle class.

This module provides a Rectangle class that inherits from BaseGeometry
with private width and height attributes validated as positive integers.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry.

    This class represents a rectangle with private width and height
    attributes that are validated as positive integers.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle with validated width and height.

        Args:
            width (int): Positive integer representing rectangle width.
            height (int): Positive integer representing rectangle height.

        Raises:
            TypeError: When width or height is not an integer.
            ValueError: When width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
