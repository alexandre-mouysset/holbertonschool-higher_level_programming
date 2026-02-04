#!/usr/bin/python3
"""BaseGeometry class module."""


class BaseGeometry:
    """A BaseGeometry class with area method."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
