#!/usr/bin/python3
"""Module with base class"""
import json


class Base:
    """manage id attribute, json encoding and decoding for subclasses
    loading to and from file for subclasses, create instance from dict"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of attributes"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string([cls.to_dictionary(obj) for obj
                                        in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string representation json_string"""
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            r1 = cls(1, 1)
            r1.update(**dictionary)
            return r1
        elif cls.__name__ == "Square":
            s1 = cls(1)
            s1.update(**dictionary)
            return s1

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                json_str = f.read()
        except:
            return []
        return [cls.create(**a_dict) for a_dict in
                cls.from_json_string(json_str)]
