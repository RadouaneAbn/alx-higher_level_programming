#!/usr/bin/python3
"""0-read_file"""


def read_file(filename=""):
    """This function reads and prints a text file to STDOUT"""
    with open(filename, 'r', encoding="utf-8") as file_0:
        for line in file_0:
            print(line, end="")
