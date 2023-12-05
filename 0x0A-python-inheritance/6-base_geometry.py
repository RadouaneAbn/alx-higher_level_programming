#!/usr/bin/python3
"""
BaseGeometry Class

Class:
    BaseGeometry: raise an exception

Usage:
    bg = BaseGeometry()
"""


class BaseGeometry:
    """
    BaseGeometry Class

    Methods:
        area(self): Raise an exception indicating that
            the area() method is not implemented.
    """
    def area(self):
        raise Exception("area() is not implemented")
