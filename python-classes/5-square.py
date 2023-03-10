#!/usr/bin/python3
"""Bin Bash for .py Files"""


class Square:
    """
    Attributes:
        size (str): The size of the square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.position
    
    @position.setter
    def position(self, value):
        if position:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for h in range(self.__size):
            for v in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")

