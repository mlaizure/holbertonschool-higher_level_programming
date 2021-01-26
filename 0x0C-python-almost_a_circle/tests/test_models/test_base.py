#!/usr/bin/python3
"""Module with unittests for Base class"""
import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """tests for Base class"""
    def test_init(self):
        """tests initialization method for Base class"""
        base = Base()
        self.assertEqual(base.id, 3)
        base = Base(None)
        self.assertEqual(base.id, 4)
        base = Base(17)
        self.assertEqual(base.id, 17)
        base = Base()
        self.assertEqual(base.id, 5)

    def test_to_json_string(self):
        """tests to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), "[{\"id\": 1}]")
        self.assertEqual(Base.to_json_string([{}, {}]), "[{}, {}]")

    def test_save_to_file(self):
        """tests save_to_file method"""
        l_objs = None
        Base.save_to_file(l_objs)
        with open("Base.json", mode='r') as f:
            self.assertEqual(f.read(), Base.to_json_string(l_objs))

        l_objs = []
        Base.save_to_file(l_objs)
        with open("Base.json", mode='r') as f:
            self.assertEqual(f.read(), Base.to_json_string(l_objs))

        l_objs = [Rectangle(1, 2, 3, 4, 99)]
        Base.save_to_file(l_objs)
        with open("Base.json", mode='r') as f:
            self.assertEqual(f.read(),
                             Base.to_json_string([l_objs[0].to_dictionary()]))

        l_objs = [Square(1), Square(2)]
        Base.save_to_file(l_objs)
        with open("Base.json", mode='r') as f:
            self.assertEqual(f.read(),
                             Base.to_json_string([l_objs[0].to_dictionary(),
                                                  l_objs[1].to_dictionary()]))

    def test_from_json_string(self):
        """tests from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string("[{\"id\": 1}]"), [{"id": 1}])
        self.assertEqual(Base.from_json_string("[{}, {}]"), [{}, {}])

    def test_create(self):
        """tests create method"""
        rec_dict = {"width": 1, "height": 2, "x": 3, "y": 4, "id": 99}
        rec_obj = Rectangle.create(**rec_dict)
        self.assertEqual(rec_obj.width, rec_dict['width'])
        self.assertEqual(rec_obj.height, rec_dict['height'])
        self.assertEqual(rec_obj.x, rec_dict['x'])
        self.assertEqual(rec_obj.y, rec_dict['y'])
        self.assertEqual(rec_obj.id, rec_dict['id'])

        squ_dict = {"size": 5, "x": 6, "y": 7, "id": 98}
        squ_obj = Square.create(**squ_dict)
        self.assertEqual(squ_obj.size, squ_dict['size'])
        self.assertEqual(squ_obj.width, squ_dict['size'])
        self.assertEqual(squ_obj.height, squ_dict['size'])
        self.assertEqual(squ_obj.x, squ_dict['x'])
        self.assertEqual(squ_obj.y, squ_dict['y'])
        self.assertEqual(squ_obj.id, squ_dict['id'])

    def test_load_from_file(self):
        """tests load_from_file method"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

        list_squ = [Square(1), Square(2, 3, 4, 99)]
        Square.save_to_file(list_squ)
        list_from = Square.load_from_file()
        self.assertEqual(type(list_from), list)
        self.assertEqual(list_from[0].size, list_squ[0].size)
        self.assertEqual(list_from[0].width, list_squ[0].width)
        self.assertEqual(list_from[0].height, list_squ[0].height)
        self.assertEqual(list_from[0].x, list_squ[0].x)
        self.assertEqual(list_from[0].y, list_squ[0].y)
        self.assertEqual(list_from[0].id, list_squ[0].id)
        self.assertEqual(list_from[1].size, list_squ[1].size)
        self.assertEqual(list_from[1].width, list_squ[1].width)
        self.assertEqual(list_from[1].height, list_squ[1].height)
        self.assertEqual(list_from[1].x, list_squ[1].x)
        self.assertEqual(list_from[1].y, list_squ[1].y)
        self.assertEqual(list_from[1].id, list_squ[1].id)
