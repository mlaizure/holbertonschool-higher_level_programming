#!/usr/bin/python3
"""Module with a class Rectangle that inherits from class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """instantiates with width and height validated by int validator in
    BaseGeometry class"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height


if __name__ == "__main__":
    Rectangle = __import__('8-rectangle').Rectangle

    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
