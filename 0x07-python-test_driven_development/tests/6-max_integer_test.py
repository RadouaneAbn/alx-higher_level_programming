#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_value(self):
        self.assertEqual(max_integer([65, 54, 98, 51, 0, -65]), 98)
        self.assertEqual(max_integer([-15, -848, -65, -2]), -2)
        self.assertEqual(max_integer([]), None)

    def test_raise(self):
        with self.assertRaises(TypeError):
            max_integer("Test for str")
        with self.assertRaises(TypeError):
            max_integer([10, 15, "School"])
        with self.assertRaises(TypeError):
            max_integer([[1, 2], [3, 4]])
        with self.assertRaises(TypeError):
            max_integer(2)