#!/usr/bin/python3
"""
add_attribute function

Usage:
    mc = MyClass()
    add_attribute(mc, "name", "Bob")
"""


def add_attribute(obj, attribute, value):
    """
    This function adds anew attribute to an object if it's possible

    Raises:
        TypeError: if the object can't have a new attribute
    """
    if "__dict__" in dir(obj):
        obj.__dict__[attribute] = value
    else:
        raise TypeError("can't add new attribute")
