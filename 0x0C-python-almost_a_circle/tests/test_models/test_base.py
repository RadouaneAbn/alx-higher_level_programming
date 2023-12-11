#!/usr/bin/python3
""" This is a unitest for Base class
"""
from models.base import Base
from inspect import isclass
import unittest


class TestBase(unittest.TestCase):
    """ Test cases for base class
    """

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

    def test_to_json_srting_method(self):
        tmp = Base.__dict__.get("to_json_string")
        self.assertIsNotNone(tmp)
        self.assertEqual(type(tmp), staticmethod)

    def test_to_json_srting_return(self):
        dict_1 = {"x": 1, "y": 2, "id": 18, "width": 10, "height": 20}
        dict_2 = {"x": 4, "y": 5, "id": 45, "width": 24, "height": 21}
        str_1_exp = "{\"x\": 1, \"y\": 2, \"id\": 18, \"width\": 10, \
\"height\": 20}"
        str_m_exp = "[{\"x\": 1, \"y\": 2, \"id\": 18, \"width\": 10, \
\"height\": 20}, {\"x\": 4, \"y\": 5, \"id\": 45, \"width\": 24, \
\"height\": 21}]"
        str_1 = Base.to_json_string(dict_1)
        str_m = Base.to_json_string([dict_1, dict_2])

        # check: input is None or empty list
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        # check the type of the return
        self.assertEqual(type(str_1), str)

        # check the if the output is the expected output
        self.assertEqual(str_1, str_1_exp)
        self.assertEqual(str_m, str_m_exp)

    def test_save_to_file_method(self):
        tmp = Base.__dict__.get("save_to_file")
        self.assertIsNotNone(tmp)
        self.assertEqual(type(tmp), classmethod)

    def test_from_json_string_method(self):
        tmp = Base.__dict__.get("from_json_string")
        self.assertIsNotNone(tmp)
        self.assertEqual(type(tmp), staticmethod)

    def test_create_method(self):
        tmp = Base.__dict__.get("create")
        self.assertIsNotNone(tmp)
        self.assertEqual(type(tmp), classmethod)

    def test_load_from_file_method(self):
        tmp = Base.__dict__.get("load_from_file")
        self.assertIsNotNone(tmp)
        self.assertEqual(type(tmp), classmethod)

    def test_save_to_file_csv_method(self):
        tmp = Base.__dict__.get("save_to_file_csv")
        self.assertIsNotNone(tmp)
        self.assertEqual(type(tmp), classmethod)

    def test_load_from_file_csv_method(self):
        tmp = Base.__dict__.get("load_from_file_csv")
        self.assertIsNotNone(tmp)
        self.assertEqual(type(tmp), classmethod)


"""
    def test_draw_method(self):
        tmp = Base.__dict__.get("draw")
        self.assertIsNotNone(tmp)
        self.assertEqual(type(tmp), staticmethod)
"""


if __name__ == '__main__':
    unittest.main()
