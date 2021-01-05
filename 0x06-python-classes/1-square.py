#!/usr/bin/python3
"""Module makes a square class with size as a private attribute"""


class Square:
    """Class with private attribute size"""
    def __init__(self, size):
        self.__size = size
