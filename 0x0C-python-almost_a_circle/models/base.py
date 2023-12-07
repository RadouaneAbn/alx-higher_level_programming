#!/usr/bin/python3
""" base """


class Base:
    """ This class assignes a an id """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This an instance of the class Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
