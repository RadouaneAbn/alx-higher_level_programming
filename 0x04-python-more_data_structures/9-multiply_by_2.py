#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    new_dict = {i: a_dictionary[i] * 2 for i in a_dictionary}
    return new_dict
