#!/usr/bin/python3
"""Python bin"""


class Rectangle:
    """Class for the Rectangle"""

    def __init__(self, width=0, height=0):
        """Private Instance"""
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        """Return 1"""
        return self.__height * self.__width

    def perimeter(self):
        """Return 2"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Instance Method for String"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            string = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    string = string + "#"
                if i < self.__height - 1:
                    string = string + '\n'
            return string
