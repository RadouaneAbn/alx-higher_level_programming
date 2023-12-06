#!/usr/bin/python3
"""8-class_to_json"""


def class_to_json(obj):
    """This function returns the dictionary description of an object"""
    return obj.__dict__
