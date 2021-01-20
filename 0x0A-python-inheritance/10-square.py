#!/usr/bin/python3
"""Module with a class Rectangle that inherits from class BaseGeometry"""


class BaseGeometry:
    """public methods area and int validator"""
    def area(self):
        """area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """makes sure value is an int and greater than zero"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


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
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """instantiates with size validated by int validator in BaseGeometry and
    area method"""
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    def area(self):
        """calculates area of square"""
        return Rectangle.area(self)


if __name__ == "__main__":
    Square = __import__('10-square').Square

    s = Square(13)

    print(s)
    print(s.area())
