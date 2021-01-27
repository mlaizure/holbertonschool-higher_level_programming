#!/usr/bin/python3
"""Module with unittests for Square class"""
import unittest
import pep8
from models.square import Square


class TestSquare(unittest.TestCase):
    """tests for Square class"""
    def test_pep8(self):
        """tests pep8 validation"""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['models/square.py'])
        self.assertEqual(res.total_errors, 0)

    def test_init(self):
        """tests square initialization"""
        squ_1 = Square(1)
        self.assertEqual(squ_1.width, 1)
        self.assertEqual(squ_1.height, 1)
        self.assertEqual(squ_1.size, 1)
        self.assertEqual(squ_1.x, 0)
        self.assertEqual(squ_1.y, 0)

        squ_2 = Square(1, 2)
        self.assertEqual(squ_2.width, 1)
        self.assertEqual(squ_2.height, 1)
        self.assertEqual(squ_2.size, 1)
        self.assertEqual(squ_2.x, 2)
        self.assertEqual(squ_2.y, 0)

        squ_3 = Square(1, 2, 3)
        self.assertEqual(squ_3.width, 1)
        self.assertEqual(squ_3.height, 1)
        self.assertEqual(squ_3.size, 1)
        self.assertEqual(squ_3.x, 2)
        self.assertEqual(squ_3.y, 3)

        squ_99 = Square(1, 2, 3, 99)
        self.assertEqual(squ_99.width, 1)
        self.assertEqual(squ_99.height, 1)
        self.assertEqual(squ_99.size, 1)
        self.assertEqual(squ_99.x, 2)
        self.assertEqual(squ_99.y, 3)
        self.assertEqual(squ_99.id, 99)

    def test_validation(self):
        """tests for valid input"""
        with self.assertRaises(TypeError):
            Square("five", 6, 7, 8)
        with self.assertRaises(TypeError):
            Square(5, None, 7, 8)
        with self.assertRaises(TypeError):
            Square(5, 6, 7.7, 8)
        with self.assertRaises(TypeError):
            Square([5, 5], 6, 7, 8)
        with self.assertRaises(TypeError):
            Square(5, 6, (7, 7), 8)
        with self.assertRaises(TypeError):
            Square(5, {6}, 7, 8)
        with self.assertRaises(TypeError):
            Square(5, 6, False, 8)

        with self.assertRaises(ValueError):
            Square(5, 6, -1, 8)
        with self.assertRaises(ValueError):
            Square(0, 6, 7, 8)
        with self.assertRaises(ValueError):
            Square(-1, 6, 7, 8)
        with self.assertRaises(ValueError):
            Square(5, -2, 7, 8)

    def test_area(self):
        """tests area method"""
        squ_1 = Square(1)
        self.assertEqual(squ_1.area(), 1)
        squ_36 = Square(6)
        self.assertEqual(squ_36.area(), 36)

    def test_str(self):
        """tests __str__ method"""
        squ_1 = Square(1, 2, 3, 99)
        self.assertEqual(str(squ_1), "[Square] (99) 2/3 - 1")
        squ_2 = Square(5, 6, 7, 100)
        self.assertEqual(str(squ_2), "[Square] (100) 6/7 - 5")

    def test_update(self):
        """tests update method"""
        squ_1 = Square(1, 1, 1, 1)

        squ_1.update(99)
        self.assertEqual(squ_1.width, 1)
        self.assertEqual(squ_1.height, 1)
        self.assertEqual(squ_1.size, 1)
        self.assertEqual(squ_1.x, 1)
        self.assertEqual(squ_1.y, 1)
        self.assertEqual(squ_1.id, 99)

        squ_1.update(99, 2)
        self.assertEqual(squ_1.width, 2)
        self.assertEqual(squ_1.height, 2)
        self.assertEqual(squ_1.size, 2)
        self.assertEqual(squ_1.x, 1)
        self.assertEqual(squ_1.y, 1)
        self.assertEqual(squ_1.id, 99)

        squ_1.update(99, 2, 3)
        self.assertEqual(squ_1.width, 2)
        self.assertEqual(squ_1.height, 2)
        self.assertEqual(squ_1.size, 2)
        self.assertEqual(squ_1.x, 3)
        self.assertEqual(squ_1.y, 1)
        self.assertEqual(squ_1.id, 99)

        squ_1.update(99, 2, 3, 4)
        self.assertEqual(squ_1.width, 2)
        self.assertEqual(squ_1.height, 2)
        self.assertEqual(squ_1.size, 2)
        self.assertEqual(squ_1.x, 3)
        self.assertEqual(squ_1.y, 4)
        self.assertEqual(squ_1.id, 99)

        squ_1.update(y=6, x=7, id=98, size=8)
        self.assertEqual(squ_1.width, 8)
        self.assertEqual(squ_1.height, 8)
        self.assertEqual(squ_1.size, 8)
        self.assertEqual(squ_1.x, 7)
        self.assertEqual(squ_1.y, 6)
        self.assertEqual(squ_1.id, 98)

    def test_to_dictionary(self):
        """tests to_dictionary method"""
        squ_1 = Square(1, 2, 3, 99)
        self.assertEqual(squ_1.to_dictionary(), {'id': 99, 'size': 1,
                                                 'x': 2, 'y': 3})
