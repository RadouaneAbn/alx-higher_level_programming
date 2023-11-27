#!/usr/bin/python3
"""
Rectangle Module

This module defines a simple class named Rectangle.

Class:
    Rectangle: Defines a rectangle.

Usage:
    new_rectangle = Rectangle() # Creates a new instance named new_rectangle.
    new_rectangle.width = Value # sets the width of the rectangle to value.
    new_rectangle.height = Value # sets the height of the rectangle to value.
    n = new_rectangle.width # Return the value of __width.
    n = new_rectangle.height # Return the value of __height.
    print(str(new_rectangle)) # Print the rectangle with the character #
    print(repr(new_rectangle)) # Print the representation of the rectangle
    del new_rectangle # Deletes the instance, and calls __del__.
    rect = bigger_or_equal(rect_1, rect_2) # returns the biggest rectangle.
"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height if the rectangle.

    Args:
        print_symbol (any): the symbol for string representation.
        number_of_instances (int): the number of instances.
    """

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle calss.

        Args:
            width (int, optional): The width of the rectangle.
            height (int, optional): The height of the rectangle.

        Raises:
            TypeError: if the width or the height is not an integer.
            ValueError: if the width or the height is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle to value.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle to value.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculates the area of a rectangle.

        Returns:
            (int): The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of a rectangle.

        Returns:
            (int): The perimeter of the rectangle or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Makes a printable string

        Returns:
            (str): the string or an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        result = []
        for n in range(self.__height):
            tmp_line = ""
            for m in range(self.__width):
                tmp_line += str(self.print_symbol)
            result.append(tmp_line)
        return ("\n".join(result))

    def __repr__(self):
        """
        Makes a string representation of the rectangle.

        Returns:
            (str): return a string representation of the rectangle
            "Rectangle(width, height)".
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        This method is automatically called when an instance of the Rectangle
        is about to be deleted.

        It prints a message indicating that a rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and return the one that's equal
            or greater area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: if rect_1 or rect_2 is not an instance of the rectangle.

        returns:
            the rectangle with the biggest area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        a, b = rect_1.area(), rect_2.area()
        if a >= b:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
