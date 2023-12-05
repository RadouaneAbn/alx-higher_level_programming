#!/usr/bin/python3
""" Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry.

    Methods:
        __init__(self, width, height):
            Initialize a new instance of the Rectangle class.
        area:
            return the area of a rectangle
        __str__:
            Returns a string representing the rectangle instance

    Usage:
        rg = Rectangle(5, 10)
    """
    def __init__(self, width, height):
        """
        Initialize a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle instance"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
