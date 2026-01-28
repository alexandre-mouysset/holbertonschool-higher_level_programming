#!/usr/bin/python3
"""Square class module."""


class Square:
    """A square with printing capability."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int): Side length (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The side length.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new side length.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square.

        Returns:
            int: The area (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters.

        Prints an empty line if size is 0.
        """
        if self.size == 0:
            print()

        else:
            for i in range(self.size):
                print("#" * self.size)
