#!/usr/bin/python3
"""2-append_write"""


def append_write(filename="", text=""):
    """This function appends a string to a text file"""
    text_size = len(text)
    with open(filename, 'a', encoding="utf-8") as file_1:
        file_1.write(text)

    return text_size
