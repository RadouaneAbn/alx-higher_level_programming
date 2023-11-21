#!/usr/bin/python3
"""
Module Name: magic_class
"""
import math


class MagicClass:
    """
     Initializes a new instance

     Attributes:
        None
    """
    def __init__(self, radius=0):
        """
        Initializes a new instance of the class.

        Args:
                radius (int, float, optional): The radius of the circle

        Raises:
             TypeError: If the radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: the circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
