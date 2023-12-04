#!/usr/bin/python3
"""
Define a Class that inherits from list.

Class:
    MyList: A custom class that inherits from the list class.

Usage:
    list_1 = MyList([3, 1, 4, 1, 5, 9, 2])
    list_1.print_sorted()
"""


class MyList(list):
    """
    A custom class that inherits from the list class.

    Methods:
    print_sorted(self):
        Print the elements of the list in sorted order.
    """
    def print_sorted(self):
        """
        Print the elements of the list in sorted order.
        """
        print(sorted(self))
