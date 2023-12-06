#!/usr/bin/python3
"""6-load_from_json_file"""
import json


def load_from_json_file(filename):
    """This function that creates an object from a JSON file"""
    with open(filename, 'r') as file_6:
        string = file_6.readline()
        obj = json.loads(string)

    return obj
