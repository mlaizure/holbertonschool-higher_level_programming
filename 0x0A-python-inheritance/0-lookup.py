#!/usr/bin/python3
"""Module with function that returns the list of availabe attributes and
methods of an object"""


def lookup(obj):
    """returns the list of available functions and attributes of an object"""
    return dir(obj)

if __name__ == "__main__":
    lookup = __import__('0-lookup').lookup

    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
