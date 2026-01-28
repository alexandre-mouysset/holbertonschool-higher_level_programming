#!/usr/bin/python3
"""Square class module."""


class Square:
    """A square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int): Side length (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the area of the square.

        Returns:
            int: The area (size squared).
        """
        return self.__size ** 2
