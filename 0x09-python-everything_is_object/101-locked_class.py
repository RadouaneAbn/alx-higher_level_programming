#!/usr/bin/python3
"""
LockedClass module

This script defines a class named LockedClass using the __slots__ mechanism.

Class:
    LockedClass: A class with a restricted set of
        attributes defined by __slots__.

Usage:
    locked_instance = LockedClass()
    locked_instance.first_name = "John"  # Valid assignment
    locked_instance.last_name = "Doe"     # Raises AttributeError
"""


class LockedClass:
    """
    A class with a restricted set of attributes defined by __slots__.
    """
    __slots__ = ['first_name']
