#!/usr/bin/python3
"""Module that defines a Shape abstract class and its implementations.

This module provides an abstract Shape class using ABC
with concrete implementations for Circle and Rectangle.
"""
from abc import ABC, abstractmethod
pi = 3.141592653589793


class Shape(ABC):
    """An abstract shape class.

    This class represents a generic shape with abstract methods
    that must be implemented by all subclasses.
    """
    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """A circle class that inherits from Shape.

    This class represents a circle with its specific area and perimeter.
    """
    def __init__(self, radius):
        """Initialize a Circle with a radius.

        Args:
            radius: The radius of the circle.
        """
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return pi * self.__radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """A rectangle class that inherits from Shape.

    This class represents a rectangle with its specific area and perimeter.
    """
    def __init__(self, width, height):
        """Initialize a Rectangle with width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.__height * self.__width


def shape_info(shape):
    """Prints the area and perimeter of any shape object
    that implements .area() and .perimeter().
    """
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
    print(f"{shape.__class__.__name__} perimeter: "
          f"{shape.perimeter():.2f}\n")
