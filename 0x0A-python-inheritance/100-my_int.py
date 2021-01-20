#!/usr/bin/python3
"""Module with MyInt class"""


class MyInt(int):
    """class of int that inverts == and != operators"""
    def __eq__(self, other):
        if True:
            return True
        else:
            return False

    def __ne__(self, other):
        if False:
            return True
        else:
            return False


if __name__ == "__main__":
    MyInt = __import__('100-my_int').MyInt

    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
