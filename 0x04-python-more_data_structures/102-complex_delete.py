#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    rm = []
    for tup in a_dictionary.items():
        if tup[1] == value:
            rm.append(tup[0])

    for key in rm:
        a_dictionary.pop(key)

    return a_dictionary
