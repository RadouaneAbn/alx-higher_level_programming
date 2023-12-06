#!/usr/bin/python3
"""4-from_json_string"""
import json


def from_json_string(my_str):
    """This function returns an object represented by JSON string"""
    return json.loads(my_str)
