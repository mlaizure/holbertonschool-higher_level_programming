#!/usr/bin/python3
"""Module with class Square that inherits from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """all attributes from Rectangle, can initialize, stringify, update, and
    dictionarify itself"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes attributes of square instance"""
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """returns a human readable string for pretty printing"""
        strg = "[Square] ({})".format(self.id)
        strg += " {}/{}".format(self.x, self.y)
        strg += " - {}".format(self.width)
        return strg

    @property
    def size(self):
        """retrieves size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            attr_list = ["id", "size", "x", "y"]
            for attr, value in zip(attr_list, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of a Square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
