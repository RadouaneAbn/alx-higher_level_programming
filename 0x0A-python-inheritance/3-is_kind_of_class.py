#!/usr/bin/python3
"""
This function checks if an object is an instance of a specified class
or is an instance of a class that inhetites from it.

Usage:
    is_kind_of_class(5, int)
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of, or if the object
    is an instance of a class that inherited from, the specified clas

    Args:
        obj (any): The object that will be checked.
        a_class : The class to check

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
