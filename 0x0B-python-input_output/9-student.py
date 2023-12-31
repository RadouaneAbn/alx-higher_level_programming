#!/usr/bin/python3
""" 9-student """


class Student:
    """ This class defines a student """

    def __init__(self, first_name, last_name, age):
        """ an instance of Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns a dictionary representation of a Student """
        return self.__dict__
