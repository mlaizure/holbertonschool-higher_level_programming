#!/usr/bin/python3
"""Module with a class Rectangle that inherits from class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """instantiates with width and height validated by int validator in
    BaseGeometry class, area and __str__ methods"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns formatted string to print"""
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)

if __name__ == "__main__":
    Rectangle = __import__('9-rectangle').Rectangle

    r = Rectangle(3, 5)

    print(r)
    print(r.area())
