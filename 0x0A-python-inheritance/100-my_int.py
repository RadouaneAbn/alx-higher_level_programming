#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """Class that inherit from int and modifies
        the behavior of equality and inequality operators."""
    def __eq__(self, other):
        """Override the equality operator and check for inequality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator and check for equality"""
        return super().__eq__(other)
