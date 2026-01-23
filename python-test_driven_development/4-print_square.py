#!/usr/bin/python3
"""
Module that prints a square using # characters.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: Size of the square (must be integer >= 0)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is negative
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
