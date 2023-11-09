#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())
    idxs = len(values)

    i = 0
    while i < idxs:
        if values[i] == value:
            a_dictionary.pop(keys[i])
            idxs = idxs - 1
        i = i + 1

    return a_dictionary
