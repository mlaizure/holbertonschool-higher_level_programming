#!/usr/bin/python3
"""Module has a function that adds two integers"""


def add_integer(a, b=98):
    """adds integers a and b, casts floats as ints, b defatuls to 98"""
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
