#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width_value):

        if not isinstance(width_value, int):
            raise TypeError("width must be an integer")

        if width_value < 0:
            raise ValueError("width must be >= 0")

        self.__width = width_value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height_value):

        if not isinstance(height_value, int):
            raise TypeError("height must be an integer")

        if height_value < 0:
            raise TypeError("height must be >= 0")

        self.__height = height_value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * self.__height) * 2)
