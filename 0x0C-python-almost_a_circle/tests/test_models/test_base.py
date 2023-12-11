#!/usr/bin/python3
"""
    This is a unitest for Base class
                                     """
from models.base import Base
from inspect import isclass
import unittest


class TestBase(unittest.TestCase):
    def test_Value(self):
        obj_1 = Base()
        obj_2 = Base()
        self.assertEqual(obj_2.id, obj_1.id + 1)
        self.assertEqual(obj_2.id, Base._Base__nb_objects)
        obj_3 = Base(98)
        self.assertEqual(obj_3.id, 98)

    def test_Type(self):
        # This will take the first id obj_4.id = 1
        self.assertTrue(isclass(Base))
        obj_4 = Base()
        self.assertTrue(type(obj_4) is Base)
        self.assertIsInstance(obj_4, Base)
        self.assertIsInstance(obj_4.id, int)

    def test_None(self):
        obj_0 = Base()
        self.assertEqual(obj_0.id, 1)
        self.assertIsNotNone(obj_0)
        self.assertIsNotNone(obj_0.id)        
        


if __name__ == '__main__':
    unittest.main()