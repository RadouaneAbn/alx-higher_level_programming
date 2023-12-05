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
        area: Raise an exception indicating that
            the area() method is not implemented.

        integer_validator: Validates value
    """
    def area(self):
        """
        Raise an exception

        Raises:
            Exception: indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valites value

        Args:
            name (str): the name of the variable storing the value
            value (int): the value that will be checked

        raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less or equal 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
