#!/usr/bin/python3
"""1-write_file"""


def write_file(filename="", text=""):
    """This function writes a string to a text file"""
    text_size = len(text)
    with open(filename, 'w', encoding="utf-8") as file_1:
        file_1.write(text)

    return text_size
