#!/usr/bin/python3
"""Module with MyInt class"""


class MyInt(int):
    """class of int that inverts == and != operators"""
    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)


if __name__ == "__main__":
    MyInt = __import__('100-my_int').MyInt

    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
