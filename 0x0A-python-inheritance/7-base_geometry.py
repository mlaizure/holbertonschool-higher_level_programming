#!/usr/bin/python3
"""Module with a class BaseGeometry with public methods area and int
validator"""


class BaseGeometry:
    """public methods area and int validator"""
    def area(self):
        """area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """makes sure value is an int and greater than zero"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
