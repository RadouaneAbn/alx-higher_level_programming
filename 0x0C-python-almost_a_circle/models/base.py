#!/usr/bin/python3
""" base module """
import json
import csv
import turtle
from os import path
import time


class Base:
    """ Base class that assignes an id to an object.

        Attributes:
            nb_objects (int): The number of objects created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize an instance of the Base class.
            Takes one argument (int).

            Args:
                id (id, optional): the id of the new object.
                if None an id will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts a list of dictionaries into a JSON string.

            Args:
                list_dictionaries (list): A list of directories.

            Return:
                str: Returns a JSON string representation of a given list.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of a list of objects
            to a JSON file.

            Args:
                list_objs (list): List of objects.
        """
        file_name = "{}.json".format(cls.__name__)
        Dict_list = []
        if list_objs is not None:
            for obj in list_objs:
                # print("==> {}".format(obj))
                Dict_list.append(obj.to_dictionary())

        with open(file_name, 'w') as f:
            f.write(Base.to_json_string(Dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ Coverts a JSON string to a list of dictionaries.

            Args:
                json_string (str): JSON string.

            Returns:
                list: A list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance of the class.

            Args:
                dictionary (dict): Dictionary of attributes 'id, width, ...'

            Returns:
                obj: The newly created instance
        """
        if cls.__name__ == "Square":
            inst = cls(1)
            inst.update(**dictionary)
            return inst
        elif cls.__name__ == "Rectangle":
            inst = cls(1, 1)
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        """ Loads a list of inctances from a file.

            Returns:
                list: List of instances.
        """
        list_inst = []
        file_name = "{}.json".format(cls.__name__)
        if path.exists(file_name):
            with open(file_name, "r") as f:
                attrs = cls.from_json_string(f.read())
            for attr in attrs:
                list_inst.append(cls.create(**attr))

        return list_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves a list of objects to a CSV file.

            Args:
                list_objs (list): List of objects.
        """
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, "w") as f:
            csv_write = csv.writer(f)

            if cls.__name__ == "Rectangle" and list_objs:
                for obj in list_objs:
                    csv_write.writerow([obj.id, obj.width, obj.height,
                                        obj.x, obj.y])
            elif cls.__name__ == "Square" and list_objs:
                for obj in list_objs:
                    csv_write.writerow([obj.id, obj.size, obj.x, obj.y])
            else:
                csv_write.writerow([])

    @classmethod
    def load_from_file_csv(cls):
        """ Loads a list of inctances from a CSV file.

            Returns:
                list: A list of inctances
        """
        list_inst = []
        rct = ["id", "width", "height", "x", "y"]
        sqr = ["id", "size", "x", "y"]
        file_name = "{}.csv".format(cls.__name__)
        if path.exists(file_name):
            with open(file_name, "r") as f:
                csv_read = csv.reader(f)

                if cls.__name__ == "Rectangle" and csv_read:
                    for lst in csv_read:
                        list_inst.append(cls.create(
                            **{key: int(itm)for key, itm in zip(rct, lst)}))
                elif cls.__name__ == "Square" and csv_read:
                    for lst in csv_read:
                        list_inst.append(cls.create(
                            **{key: int(itm) for key, itm in zip(sqr, lst)}))

        return list_inst

    def draw(list_rectangles, list_squares):
        """ Draw rectangles and squares on a turtle screen.

            Args:
                list_rectangles (list): List of rectangle objects
                list_squares (list): List of squares
        """
        import random
        colors = ['red', 'yellow', 'grey', 'orange', 'pink', 'green', 'cyan',
                  'gold', 'purple', 'blue', 'black', 'brown', 'Lime']
        point = turtle.Turtle()
        point.pen(pensize=2)
        point.speed(1)

        for rec in list_rectangles:
            point.fillcolor(random.choice(colors))
            point.goto(rec.x, rec.y)
            point.pendown()
            point.begin_fill()
            point.forward(rec.width)
            point.left(90)
            point.forward(rec.height)
            point.left(90)
            point.forward(rec.width)
            point.left(90)
            point.forward(rec.height)
            point.end_fill()
            point.left(90)
            point.penup()

        for sqr in list_squares:
            point.fillcolor(random.choice(colors))
            point.goto(sqr.x, sqr.y)
            point.pendown()
            point.begin_fill()
            point.forward(sqr.size)
            point.left(90)
            point.forward(sqr.size)
            point.left(90)
            point.forward(sqr.size)
            point.left(90)
            point.forward(sqr.size)
            point.end_fill()
            point.left(90)
            point.penup()

        time.sleep(5)
