#!/usr/bin/python3
"""Rectangle class module."""


class Rectangle:
    """A rectangle with width and height attributes."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return the width."""
        return self.__width

    @width.setter
    def width(self, width_value):
        """Set width (must be a positive integer)."""
        if not isinstance(width_value, int):
            raise TypeError("width must be an integer")

        if width_value < 0:
            raise ValueError("width must be >= 0")

        self.__width = width_value

    @property
    def height(self):
        """Return the height."""
        return self.__height

    @height.setter
    def height(self, height_value):
        """Set height (must be a positive integer)."""
        if not isinstance(height_value, int):
            raise TypeError("height must be an integer")

        if height_value < 0:
            raise ValueError("height must be >= 0")

        self.__height = height_value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Return a string representation of the rectangl using print_symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = [str(self.print_symbol) * self.__width
                     for _ in range(self.__height)]
        return "\n".join(rectangle)

    def __repr__(self):
        """Return a formal string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when the rectangle is deleted.

        Decrement the number_of_instances counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the biggest area.

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle instance.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
