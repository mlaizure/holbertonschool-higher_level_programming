#!/usr/bin/python3
"""Module makes a square class with size as a private attribute"""


class Square:
    """Class with private attribute size with guards"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
