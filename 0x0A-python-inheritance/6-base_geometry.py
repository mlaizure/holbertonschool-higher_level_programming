#!/usr/bin/python3
"""Module with a class BaseGeometry with public method area"""


class BaseGeometry:
    """public method area"""
    def area(self):
        """area() is not implemented"""
        raise Exception("area() is not implemented")

if __name__ == "__main__":
    BaseGeometry = __import__('6-base_geometry').BaseGeometry

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
