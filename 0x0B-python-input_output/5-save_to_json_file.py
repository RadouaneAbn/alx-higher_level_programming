#!/usr/bin/python3
"""5-save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes a representation of my_obj to json file"""
    with open(filename, 'w') as file_5:
        string = json.dumps(my_obj)
        file_5.write(string)
