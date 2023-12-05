#!/usr/bin/python3
"""Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherit from rectangle"""

    def __init__(self, size):
        """Initialize a new instance of the Square class"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the Square"""
        return super().area()

    def __str__(self):
        """returns a string representation of the Square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
