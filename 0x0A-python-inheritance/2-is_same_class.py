#!/usr/bin/python3
"""
This function checks if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if the given object is an instance of the specified class.

    Args:
        obj (any): The object that will be checked.
        a_class : The class to check

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
