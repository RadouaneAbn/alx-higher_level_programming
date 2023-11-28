#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_value(self):
        """ Test random order list """
        self.assertEqual(max_integer([65, 54, 98, 51, 0, -65]), 98)

        """ Test max integer at the beginning """
        self.assertEqual(max_integer([98, 65, 54, 51, 0, -65]), 98)

        """ Test max integer at the end """
        self.assertEqual(max_integer([65, 54, 51, 0, -65, 98]), 98)

        """ Test negative integers list """
        self.assertEqual(max_integer([-15, -848, -65, -2]), -2)

        """ Test empty list """
        self.assertEqual(max_integer([]), None)

    def test_raise(self):
        """ Test a string """
        with self.assertRaises(TypeError):
            max_integer("Test for str")

        """ Test a list with a string(s) in it """
        with self.assertRaises(TypeError):
            max_integer([10, 15, "School"])

        """ Test a list of lists """
        with self.assertRaises(TypeError):
            max_integer([[1, 2], [3, 4]])

        """ Test one integer """
        with self.assertRaises(TypeError):
            max_integer(2)

        with self.assertRaises(TypeError):
            max_integer()


if __name__ == '__main__':
    unittest.main()
