#!/usr/bin/python3
"""Module with a class Rectangle defined by width and height properties"""


class Rectangle:
    """Rectangle class with int width and height properties and methods that
    return area and perimeter and str and repr method"""
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

    def __str__(self):
        """returns string of rectangle made of #s"""
        str = ""
        if self.__height == 0 or self.__width == 0:
            return str
        else:
            for i in range(self.__height):
                str += "{}\n".format("#" * self.__width)
            return str[:-1]

    def __repr__(self):
        """returns string representation of rectangle that can be parsed by
        eval"""
        str = "Rectangle({}, {})".format(self.__width, self.__height)
        return str

if __name__ == "__main__":
    Rectangle = __import__('4-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
