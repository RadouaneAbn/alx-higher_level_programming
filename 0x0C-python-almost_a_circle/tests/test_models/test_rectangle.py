#!/usr/bin/python3
"""
    This is a unitest for Rectangle class
                                          """
from models.base import Base
from models.rectangle import Rectangle
from inspect import isclass
import unittest


class TestRectangle(unittest.TestCase):
    def test_Class(self):
        self.assertTrue(isclass(Rectangle))
    
    def test_SubClass(self):
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(issubclass(Base, Rectangle))

    def test_Instance(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)
        self.assertTrue(type(r) is Rectangle)
        #self.assertEqual((r._Rectangle__width == r.height), 1)

        


if __name__ == '__main__':
    unittest.main()