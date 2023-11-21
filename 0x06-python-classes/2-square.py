#!/usr/bin/python3

"""
Module Name: square

This module defines a class named Square that represents a square

Class:
    Square: Defines a square with a specified size

Sttributes:
    None

Usage:
    new_square = Square(n) # creates a new instance named new_square
    with a size of n
"""


class Square:
    """
    Initializes a new instance of the Square class with a 'size'

    Attributes:
        __size (int): The size of the square
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class

        Args:
            size (int, optional): The size of the square.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
