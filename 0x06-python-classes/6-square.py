#!/usr/bin/python3
"""
Module Name: square

This module defines a class named Square that represents a square

Class:
    Square: Defines a square with a specified size

Attributes:
    None

Usage:
    new_square = Square(n) # creates a new instance named new_square
    with a size of n
    area_of_square = new_square.area() # calculates the area of the square
    new_square = Square(n, (x, y)) # creats a new instance named new_square
    with a size of n at position (x, y)
"""


class Square:
    """
    Initializes a new instance of the Square class with a 'size'.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): the position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square.
            position (tuple, optional)

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2\
           or type(position[0]) is not int or type(position[1]) is not int\
           or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size (value) of a square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Gets the position of the square

        Returns:
            tuple: A tuple representiong the position ad (x, y)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position (value) of the square.

        Args:
            value (tuple): A tuple of two positive integers representing
            teh new position.

        Raises:
            TypeError: if value is not a tuple of two positive integers.

        """
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1]) is not int\
           or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and return the current square area.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square with the character # or an empty line
            if the size is equal to 0 at a specific position

        Returns:
            None
        """
        if self.__size == 0:
            print()

        for y in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end="")
            print()
