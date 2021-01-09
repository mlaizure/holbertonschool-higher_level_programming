#!/usr/bin/python3
"""Module that has unittest for the 6-max_integer module"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests function that returns the max int in a list of ints"""
    def test_max(self):
        """Tests when valid input is given"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 4, 3, 3, 2]), 4)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([-5, -2]), -2)

    def test_empty(self):
        """Tests with empty list (should return None)"""
        self.assertIsNone(max_integer([]))

    def test_error(self):
        """Tests error raised when invalid input is given"""
        self.assertRaises(Exception, max_integer, ["test", 2, 3])
        self.assertRaises(Exception, max_integer, [{1}, 2, 3])
