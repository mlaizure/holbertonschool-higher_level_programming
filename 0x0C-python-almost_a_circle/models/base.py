#!/usr/bin/python3
"""Module with base class"""
import json
import csv


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
        if not list_objs:
            list_objs = []
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string([obj.to_dictionary() for obj
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
        except FileNotFoundError:
            return []
        return [cls.create(**a_dict) for a_dict in
                cls.from_json_string(json_str)]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes csv string representation of list_objs to file"""
        filename = "{}.csv".format(cls.__name__)
        if not list_objs:
            list_objs = []
        with open(filename, mode='w', encoding='utf-8') as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerows([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances from a csv file"""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fieldnames = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(f, fieldnames=fieldnames)
                return [cls.create(**{key: int(value) for key, value
                                      in a_dict.items()}) for a_dict in reader]
        except FileNotFoundError:
            return []
