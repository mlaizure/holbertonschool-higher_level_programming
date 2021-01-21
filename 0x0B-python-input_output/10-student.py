#!/usr/bin/python3
"""Module with class Student"""


class Student:
    """class with first and last name and age attributes and public method
    that retrieves a dictionary representation of a Student instance"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict representation of a Student instance"""
        my_attrs = ["first_name", "last_name", "age"]
        if type(attrs) is list:
            if all(isinstance(item, str) for item in attrs):
                attrs = set(attrs).intersection(my_attrs)
                return {item: getattr(self, item) for item in attrs}
        else:
            return self.__dict__
