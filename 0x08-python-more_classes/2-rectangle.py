#!/usr/bin/python3
"""Module with a class Rectangle defined by width and height properties"""


class Rectangle:
    """Rectangle class with int width and height properties
    and methods that return area and perimeter"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

if __name__ == "__main__":
    Rectangle = __import__('2-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
                                            my_rectangle.perimeter()))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
                                            my_rectangle.perimeter()))
