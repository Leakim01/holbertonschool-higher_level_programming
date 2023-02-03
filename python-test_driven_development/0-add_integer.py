#!/usr/bin/python3
"""File to add 2 Integers Together"""


def add_integer(a, b=98):
    """The Function"""
    try:
        result = a + b
        return int(result)
    except TypeError:
        if type(a) is not int:
            return "a must be an integer"
        else:
            return "b must be an integer"