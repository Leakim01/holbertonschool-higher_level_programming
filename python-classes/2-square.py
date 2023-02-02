#!/usr/bin/python3
"""Bin Bash for .py Files"""


class Square:
    """
    Attributes:
        size (str): The size of the square"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
