#!/usr/bin/python3
"""Module with a class Rectangle defined by width and height properties"""


class Rectangle:
    """Rectangle class with int width and height properties and class
    properties of number of instances and print symbol and methods that return
    area and perimeter and str and repr and del method"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """returns string of rectangle made of print_symbol"""
        strg = ""
        if self.__height == 0 or self.__width == 0:
            return strg
        else:
            for i in range(self.__height):
                strg += "{}\n".format(str(self.print_symbol) * self.__width)
            return strg[:-1]

    def __repr__(self):
        """returns string representation of rectangle that can be parsed by
        eval"""
        strg = "Rectangle({}, {})".format(self.__width, self.__height)
        return strg

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

if __name__ == "__main__":
    Rectangle = __import__('7-rectangle').Rectangle

    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    print("--")
    my_rectangle_1.print_symbol = "&"
    print(my_rectangle_1)
    print("--")

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
    print("--")
    Rectangle.print_symbol = "C"
    print(my_rectangle_2)
    print("--")

    my_rectangle_3 = Rectangle(7, 3)
    print(my_rectangle_3)

    print("--")

    my_rectangle_3.print_symbol = ["C", "is", "fun!"]
    print(my_rectangle_3)

    print("--")
