#!/usr/bin/python3
"""Module with class Student"""


class Student:
    """class with first and last name and age attributes and public method
    that retrieves a dictionary representation of a Student instance"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dict representation of a Student instance"""
        return self.__dict__
