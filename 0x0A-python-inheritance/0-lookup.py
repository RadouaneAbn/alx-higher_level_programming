#!/usr/bin/python3
"""
Object Lookup Function

Usage:
    lookup(int)
"""


def lookup(obj):
    """
    This function returns a list of available
    attributes and methods of an object

    Args:
        obj (any): The object

    Returns:
        List of available attributes and methods of obj (object)
    """
    return dir(obj)
