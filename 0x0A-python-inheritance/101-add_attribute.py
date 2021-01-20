#!/usr/bin/python3
"""Module with function that adds a new attribute to an object if possible"""


def add_attribute(obj, name, value):
    """function that adds a new attribute to an object if possible"""
    if "__dict__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
