#!/usr/bin/python3
"""Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square which inherit from Rectangle"""

    def __init__(self, size):
        """Initialisation method"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size)**2

    def __str__(self):
        """Prints the rectangle (square)"""
        return ("[Rectangle]".format(self.__size))
