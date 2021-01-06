#!/usr/bin/python3
"""Module makes a square class with size as a private attribute"""


class Square:
    """Class with private attribute size with guards
    calculates and can compare square areas"""
    def __init__(self, size=0):
            self.size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False

    def __ne__(self, other):
        if self.area() != other.area():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.area() < other.area():
            return True
        else:
            return False

    def __le__(self, other):
        if self.area() <= other.area():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.area() > other.area():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.area() >= other.area():
            return True
        else:
            return False
