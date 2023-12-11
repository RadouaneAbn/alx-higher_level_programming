#!/usr/bin/python3
""" Rectangle module """
from .base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base class,
        and creates or modifies a rectangle.

        Attributes:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize an instance of the Rectangle class.

            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
                x (int, optional): The x-coordinate of the rectangle.
                y (int, optional): The y-coordinate of the rectangle.
                id (int, optional): The id of the rectangle.

            Raises:
                TypeError: If width, height, x, or y are not integers.
                ValueError: If width or height is less than or equal to 0,
                or if x or y is less than 0.
       """
        for val, val_name in zip([width, height, x, y],
                                 ["width", "height", "x", "y"]):
            if not isinstance(val, int):
                raise TypeError(val_name + " must be an integer")

        for val, val_name in zip([width, height], ["width", "height"]):
            if val <= 0:
                raise ValueError(val_name + " must be > 0")

        for val, val_name in zip([x, y], ["x", "y"]):
            if val < 0:
                raise ValueError(val_name + " must be >= 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Gets the width of the rectangle.

            Returns:
                int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle.

            Args:
                value (int): The new width of the rectangle.

            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is less than or equal to 0.
       """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of the rectangle.

            Returns:
                int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle.

            Args:
                value (int): The new height of the rectangle.

            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets the x-coordinate of the rectangle.

            Returns:
                int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the x-coordinate of the rectangle.

            Args:
                value (int): The new x-coordinate of the rectangle.

            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets the y-coordinate of the rectangle.

            Returns:
                int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the y-coordinate of the rectangle.

            Args:
                value (int): The new y-coordinate of the rectangle.

            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate the area of the rectangle.

            Returns:
                int: The area of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """ Display the rectangle.
        """
        print("{}".format("\n" * self.__y), end='')
        for i in range(self.__height):
            print("{}".format(" " * self.__x), end='')
            print("#" * self.__width)

    def __str__(self):
        """ Return a string representation of the rectangle.

            Returns:
                str: A string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Update the attributes of the rectangle.

            Args:
                *args (list): List of parameters.
                **kwargs (dict): dictionary.
        """
        func = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, func[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Convert the rectangle to a dictionary.

            Returns:
                dict: A dictionary representation of the rectangle.
           """
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
                }
