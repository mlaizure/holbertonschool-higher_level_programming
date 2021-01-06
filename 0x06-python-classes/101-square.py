#!/usr/bin/python3
"""Module makes a square class with size as a private attribute"""


class Square:
    """Class with private attributes size and position
    Can calculate area of square or print it with hashes"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position of square"""
        if not isinstance(value, tuple) or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for num in value:
            if not isinstance(num, int) or num < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints square with # to stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """makes print have the same behavior as my_print"""
        str = ""
        if self.__size == 0:
            return str
        else:
            for i in range(self.__position[1]):
                str += '\n'
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    str += ' '
                for i in range(self.__size):
                    str += '#'
                str += '\n'
        return str[:-1]
