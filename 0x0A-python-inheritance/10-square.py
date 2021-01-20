#!/usr/bin/python3
"""Module with a class Rectangle that inherits from class BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """instantiates with size validated by int validator in BaseGeometry and
    area method"""
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

#    def area(self):
#        """calculates area of square"""
#        return Rectangle.area(self)


if __name__ == "__main__":
    Square = __import__('10-square').Square

    s = Square(13)

    print(s)
    print(s.area())
