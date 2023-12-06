#!/usr/bin/python3
"""
7-add_item
This script adds all arguments to python list and save the list in a file
"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
py_list = []

try:
    py_list = load_from_json_file(filename)
except FileNotFoundError:
    pass

for arg in argv[1:]:
    py_list.append(arg)

save_to_json_file(py_list, filename)
