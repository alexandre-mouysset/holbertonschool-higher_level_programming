#!/usr/bin/python3
"""BaseGeometry class module."""


class BaseGeometry:
    """A BaseGeometry class with area method."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
