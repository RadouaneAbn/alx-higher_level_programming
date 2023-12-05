#!/usr/bin/python3
""" Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry.

    Methods:
        __init__(self, width, height):
        Initialize a new instance of the Rectangle class.

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
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
