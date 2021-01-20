#!/usr/bin/python3
"""Module with function that returns True if the object is an instance of a
class that inherited (directly or indirectly) from the specified class;
otherwise False"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False"""
    if type(obj) == a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False

if __name__ == "__main__":
    inherits_from = __import__('4-inherits_from').inherits_from

    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
