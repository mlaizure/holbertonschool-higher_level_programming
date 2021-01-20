#!/usr/bin/python3
"""Module with function that returns True if the object is an instance of the
specified class, otherwise False"""


def is_same_class(obj, a_class):
    """returns True if the object is an instance of the specified class,
    otherwise False"""
    if type(obj) == a_class:
        return True
    else:
        return False

if __name__ == "__main__":
    is_same_class = __import__('2-is_same_class').is_same_class

    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
