#!/usr/bin/python3
"""Module has a function that prints a square with #s"""


def print_square(size):
    """prints a square of length size using # characters"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("{}".format(size * '#'))
