#!/usr/bin/python3
"""
    This is a unitest for Square class
                                          """
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from inspect import isclass
import unittest
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base.__nb_objects = 0

    def test_Class(self):
        self.assertTrue(isclass(Square))

    def test_SubClass(self):
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(issubclass(Base, Square))

    def test_Instance(self):
        r = Square(1)
        self.assertIsInstance(r, Square)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)
        self.assertTrue(type(r) is Square)

    def test_raises(self):

        # TypeError Exception
        with self.assertRaises(TypeError) as err:
            r = Square("string")
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(TypeError) as err:
            r2 = Square(5, "string")
        self.assertEqual(str(err.exception), "x must be an integer")

        with self.assertRaises(TypeError) as err:
            r3 = Square(5, 5, "string")
        self.assertEqual(str(err.exception), "y must be an integer")

        # ValueError Exception
        with self.assertRaises(ValueError) as err:
            r = Square(-5)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(ValueError) as err:
            r = Square(0)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(ValueError) as err:
            r2 = Square(5, -5)
        self.assertEqual(str(err.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as err:
            r3 = Square(5, 5, -5)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_args(self):
        r_1 = Square(1)
        self.assertEqual(r_1.id, r_1._Base__nb_objects)
        r_2 = Square(1, 2)
        self.assertEqual(r_2.id, r_2._Base__nb_objects)
        r_3 = Square(1, 2, 3, 98)

        self.assertEqual(r_1._Rectangle__width, 1)
        self.assertEqual(r_1._Rectangle__x, 0)
        self.assertEqual(r_1._Rectangle__y, 0)

        self.assertEqual(r_3._Rectangle__width, 1)
        self.assertEqual(r_3._Rectangle__x, 2)
        self.assertEqual(r_3._Rectangle__y, 3)
        self.assertEqual(r_3.id, 98)

    def test_setter_getter(self):
        r_1 = Square(1, 3, 4, 98)
        r_1.size = 14
        self.assertEqual(r_1.size, 14)
        r_1.x = 10
        self.assertEqual(r_1.x, 10)
        r_1.y = 20
        self.assertEqual(r_1.y, 20)

    def test_area(self):
        r_1 = Square(15)
        self.assertEqual(r_1.area(), 225)

    def test_diplay(self):
        r_1 = Square(2)
        r_2 = Square(4, 3)
        r_3 = Square(3, 0, 3)
        original_stdout = sys.stdout
        output_buffer = StringIO()

        sys.stdout = output_buffer
        r_1.display()
        r_1_got = output_buffer.getvalue()
        sys.stdout = original_stdout

        output_buffer = StringIO()
        sys.stdout = output_buffer
        r_2.display()
        r_2_got = output_buffer.getvalue()
        sys.stdout = original_stdout

        output_buffer = StringIO()
        sys.stdout = output_buffer
        r_3.display()
        r_3_got = output_buffer.getvalue()
        sys.stdout = original_stdout

        self.assertEqual(r_1_got, "##\n##\n")
        self.assertEqual(r_2_got, "   ####\n   ####\n   ####\n   ####\n")
        self.assertEqual(r_3_got, "\n\n\n###\n###\n###\n")

    def test_str(self):
        r = Square(12, 15, 33, 198)
        self.assertEqual(str(r), "[Square] (198) 15/33 - 12")

    def test_to_dictionary(self):
        r = Square(142, 15, 33, 198)
        self.assertEqual(r.to_dictionary(), {'id': 198, 'x': 15, 'size': 142,
                                             'y': 33})


if __name__ == '__main__':
    unittest.main()
