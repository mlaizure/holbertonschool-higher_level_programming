#!/usr/bin/python3
"""Module makes a MagicClass that does exactly the same as some specified
byte code"""

import math


class MagicClass:
    """Class that does some stuff to a circle I assume"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.py * self.__radius
