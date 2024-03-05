#!/usr/bin/python3
"""
This script contains a fucntion that finds peak in a list integers
"""


def find_peak(list_of_integers):
    """ This function finds the peak """
    if not list_of_integers:
        return None
    left, right = 0, len(list_of_integers) - 1

    while left <= right:
        m = left + ((right - left) // 2)

        if m > 0 and list_of_integers[m] < list_of_integers[m - 1]:
            right = m - 1
        elif m < len(list_of_integers) - 1 and \
                list_of_integers[m] < list_of_integers[m + 1]:
            left = m + 1
        else:
            # The peak is found
            return list_of_integers[m]
