#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    result, div = 0, 0
    for tup in my_list:
        result += tup[0] * tup[1]
        div += tup[1]

    return result / div if div != 0 else 0
