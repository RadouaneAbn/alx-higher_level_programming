#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx in range(len(my_list)):
        my_list[idx:idx + 1] = []
    return my_list
