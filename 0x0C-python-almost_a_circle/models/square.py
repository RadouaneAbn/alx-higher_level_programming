#!/usr/bin/python3
""" Square module """
from .rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle class,
        and creates or modifies a square.

        Attributes:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize an instance of the Square class.

            Args:
                width (int): The size of the square.
                x (int, optional): The x-coordinate of the square.
                y (int, optional): The y-coordinate of the square.
                id (int, optional): The id of the square.

            Raises:
                TypeError: If size, x, or y are not integers.
                ValueError: If size is less than or equal to 0,
                or if x or y is less than 0.
       """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """ Update the attributes of the square.

            Args:
                *args (list): List of parameters.
                **kwargs (dict): dictionary.
        """
        if args:
            func = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, func[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Return a string representation of the square.

            Returns:
                str: A string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ Gets the size of the square.

            Returns:
                int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, size):
        """ Set the size of the square.

            Args:
                size (int): The new size of the square.

            Raises:
                TypeError: If the size is not an integer.
                ValueError: If the size is less than or equal to 0.
        """
        self.width = size
        self.height = size

    def to_dictionary(self):
        """ Convert the square to a dictionary.

            Returns:
                dict: A dictionary representation of the square.
        """
        return {
                "id": self.id,
                "x": self.x,
                "size": self.width,
                "y": self.y
                }
