#!/usr/bin/python3
""" This is a unitest for Base class
"""
from models.base import Base
from inspect import isclass
import os
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

    ########################################################
    #              Test to_json_srting method              #
    ########################################################

    def test_method(self):
        """ Check the method
        """
        tmp = Base.__dict__.get("to_json_string")
        self.assertIsNotNone(tmp,
                             "Base doesn't have a 'to_json_string' method")
        self.assertEqual(type(tmp), staticmethod,
                         "to_json_string is not a static method")

        def test_return(self):
            """ Check for the ouput of the method
        """
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

    ########################################################
    #               Test save_to_file method               #
    ########################################################

    def test_method(self):
        """ Check the method
        """
        tmp = Base.__dict__.get("save_to_file")
        self.assertIsNotNone(tmp,
                             "Base doesn't have a 'save_to_file' method")
        self.assertEqual(type(tmp), classmethod,
                         "save_to_file is not a classmethod method")

    ########################################################
    #             Test from_json_string method             #
    ########################################################

    def test_method(self):
        """ Check the method
        """
        tmp = Base.__dict__.get("from_json_string")
        self.assertIsNotNone(tmp,
                             "Base doesn't have a 'from_json_string' method")
        self.assertEqual(type(tmp), staticmethod,
                         "from_json_string is not a staticmethod method")

    ########################################################
    #                  Test create method                  #
    ########################################################

    def test_method(self):
        """ Check the method
        """
        tmp = Base.__dict__.get("create")
        self.assertIsNotNone(tmp,
                             "Base doesn't have a 'create' method")
        self.assertEqual(type(tmp), classmethod,
                         "create is not a classmethod method")

    ########################################################
    #              Test load_from_file method              #
    ########################################################

    def test_method(self):
        """ Check the method
        """
        tmp = Base.__dict__.get("load_from_file")
        self.assertIsNotNone(tmp,
                             "Base doesn't have a 'load_from_file' method")
        self.assertEqual(type(tmp), classmethod,
                         "load_from_file is not a classmethod method")

    ########################################################
    #             Test save_to_file_csv method             #
    ########################################################

    def test_method(self):
        """ Check the method
        """
        tmp = Base.__dict__.get("save_to_file_csv")
        self.assertIsNotNone(tmp,
                             "Base doesn't have a 'save_to_file_csv' method")
        self.assertEqual(type(tmp), classmethod,
                         "save_to_file_csv is not a classmethod method")

    ########################################################
    #            Test load_from_file_csv method            #
    ########################################################

    def test_method(self):
        """ Check the method
        """
        tmp = Base.__dict__.get("load_from_file_csv")
        self.assertIsNotNone(tmp,
                             "Base doesn't have a 'load_from_file_csv' method")
        self.assertEqual(type(tmp), classmethod,
                         "load_from_file_csv is not a classmethod method")

    ########################################################
    #                   Test draw method                   #
    ########################################################

    def test_method(self):
        """ Check the method
        """
        tmp = Base.__dict__.get("draw")
        self.assertIsNotNone(tmp,
                             "Base doesn't have a 'draw' method")
        self.assertEqual(type(tmp), staticmethod,
                         "draw is not a staticmethod method")

        if __name__ == '__main__':
            unittest.main()
