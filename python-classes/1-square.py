#!/usr/bin/python3
"""
Module defining a simple Square class.
"""


class Square:
    """
    Represents a square with a private size attribute.
    """
    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size
