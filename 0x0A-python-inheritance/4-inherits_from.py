#!/usr/bin/python3
"""
inherits_from Function

This function checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the given object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj (any): The object that will be checked.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
            False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
