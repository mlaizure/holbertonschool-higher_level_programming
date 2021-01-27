#!/usr/bin/python3
"""Module with unittests for Rectangle class"""
import unittest
import pep8
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests for Rectangle class"""
    def test_pep8(self):
        """tests pep8 validation"""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(res.total_errors, 0)

    def test_init(self):
        """tests rectangle initialization"""
        rec_1 = Rectangle(1, 2)
        self.assertEqual(rec_1.width, 1)
        self.assertEqual(rec_1.height, 2)
        self.assertEqual(rec_1.x, 0)
        self.assertEqual(rec_1.y, 0)

        rec_2 = Rectangle(1, 2, 3)
        self.assertEqual(rec_2.width, 1)
        self.assertEqual(rec_2.height, 2)
        self.assertEqual(rec_2.x, 3)
        self.assertEqual(rec_2.y, 0)

        rec_3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rec_3.width, 1)
        self.assertEqual(rec_3.height, 2)
        self.assertEqual(rec_3.x, 3)
        self.assertEqual(rec_3.y, 4)

        rec_99 = Rectangle(1, 2, 3, 4, 99)
        self.assertEqual(rec_99.width, 1)
        self.assertEqual(rec_99.height, 2)
        self.assertEqual(rec_99.x, 3)
        self.assertEqual(rec_99.y, 4)
        self.assertEqual(rec_99.id, 99)

    def test_validation(self):
        """tests for valid input"""
        with self.assertRaises(TypeError):
            Rectangle("five", 6, 7, 8, 9)
        with self.assertRaises(TypeError):
            Rectangle(5, None, 7, 8, 9)
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 7.7, 8, 9)
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 7, [8, 8], 9)
        with self.assertRaises(TypeError):
            Rectangle((5, 5), 6, 7, 8, 9)
        with self.assertRaises(TypeError):
            Rectangle(5, {6}, 7, 8, 9)
        with self.assertRaises(TypeError):
            Rectangle(5, 6, True, 8, 9)

        with self.assertRaises(ValueError):
            Rectangle(5, 6, -1, 8, 9)
        with self.assertRaises(ValueError):
            Rectangle(5, 6, 7, -2, 9)
        with self.assertRaises(ValueError):
            Rectangle(0, 6, 7, 8, 9)
        with self.assertRaises(ValueError):
            Rectangle(5, -1, 7, 8, 9)

    def test_area(self):
        """tests area method"""
        rec_1 = Rectangle(1, 1)
        self.assertEqual(rec_1.area(), 1)
        rec_42 = Rectangle(6, 7)
        self.assertEqual(rec_42.area(), 42)

    def test_str(self):
        """tests __str__ method"""
        rec_1 = Rectangle(1, 2, 3, 4, 99)
        self.assertEqual(str(rec_1), "[Rectangle] (99) 3/4 - 1/2")
        rec_2 = Rectangle(5, 6, 7, 8, 100)
        self.assertEqual(str(rec_2), "[Rectangle] (100) 7/8 - 5/6")

    def test_update(self):
        """tests update method"""
        rec_1 = Rectangle(1, 1, 1, 1, 1)

        rec_1.update(99)
        self.assertEqual(rec_1.width, 1)
        self.assertEqual(rec_1.height, 1)
        self.assertEqual(rec_1.x, 1)
        self.assertEqual(rec_1.y, 1)
        self.assertEqual(rec_1.id, 99)

        rec_1.update(99, 2)
        self.assertEqual(rec_1.width, 2)
        self.assertEqual(rec_1.height, 1)
        self.assertEqual(rec_1.x, 1)
        self.assertEqual(rec_1.y, 1)
        self.assertEqual(rec_1.id, 99)

        rec_1.update(99, 2, 3)
        self.assertEqual(rec_1.width, 2)
        self.assertEqual(rec_1.height, 3)
        self.assertEqual(rec_1.x, 1)
        self.assertEqual(rec_1.y, 1)
        self.assertEqual(rec_1.id, 99)

        rec_1.update(99, 2, 3, 4)
        self.assertEqual(rec_1.width, 2)
        self.assertEqual(rec_1.height, 3)
        self.assertEqual(rec_1.x, 4)
        self.assertEqual(rec_1.y, 1)
        self.assertEqual(rec_1.id, 99)

        rec_1.update(99, 2, 3, 4, 5)
        self.assertEqual(rec_1.width, 2)
        self.assertEqual(rec_1.height, 3)
        self.assertEqual(rec_1.x, 4)
        self.assertEqual(rec_1.y, 5)
        self.assertEqual(rec_1.id, 99)

        rec_1.update(y=6, x=7, id=98, width=8, height=9)
        self.assertEqual(rec_1.width, 8)
        self.assertEqual(rec_1.height, 9)
        self.assertEqual(rec_1.x, 7)
        self.assertEqual(rec_1.y, 6)
        self.assertEqual(rec_1.id, 98)

    def test_to_dictionary(self):
        """tests to_dictionary method"""
        rec_1 = Rectangle(1, 2, 3, 4, 99)
        self.assertEqual(rec_1.to_dictionary(), {'id': 99, 'width': 1,
                                                 'height': 2, 'x': 3, 'y': 4})
