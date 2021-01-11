#!/usr/bin/python3
"""Module makes an empty class"""


class Rectangle:
    """Empty class"""
    pass

if __name__ == "__main__":
    Rectangle = __import__('0-rectangle').Rectangle

    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)
