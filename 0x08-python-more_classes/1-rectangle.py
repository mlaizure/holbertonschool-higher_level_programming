#!/usr/bin/python3
"""Module with a class Rectangle defined by width and height properties"""


class Rectangle:
    """Rectangle class with int width and height properties"""
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


if __name__ == "__main__":
    Rectangle = __import__('1-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
