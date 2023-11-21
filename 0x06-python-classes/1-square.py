#!/usr/bin/python3
"""
Module Name: square_module

This module defines a simple class named Square.

Class:
    Square: Defines a square.

Attributes:
    None

Usage:
    new_square = Square(n) # creates a new instance named new_square
    with a size of n
"""
class Square:
    """
    Initializes a new instance of the Square class with a 'size'

    Args:
        __size (int): The size of the square.

    Returns:
        None
    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.__size = size
