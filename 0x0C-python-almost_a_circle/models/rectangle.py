#!/usr/bin/python3
"""Module with Rectangle class that inerits from Base class"""
from models.base import Base


class Rectangle(Base):
    """Private attributes width, height, x, and y"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """inititalizes class attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """retrieves width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """retrieves x positional coordinate of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x positional coordinate of rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """retrieves y positional coordinate of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y positional coordinate of rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the char #"""
        strg = ""
        for i in range(self.__y):
            strg += "\n"
        for i in range(self.__height):
            strg += "{}{}\n".format(" " * self.__x, "#" * self.__width)
        print(strg, end="")

    def __str__(self):
        """returns a human readable string for pretty printing"""
        strg = "[Rectangle] ({})".format(self.id)
        strg += " {}/{}".format(self.__x, self.__y)
        strg += " - {}/{}".format(self.__width, self.__height)
        return strg

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            attr_list = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attr_list, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
