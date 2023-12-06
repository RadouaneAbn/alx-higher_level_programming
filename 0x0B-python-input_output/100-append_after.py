#!/usr/bin/python3
""" 100-append_after """


def append_after(filename="", search_string="", new_string=""):
    """ This function inserts a line of text to a file """

    with open(filename, 'r', encoding="utf-8") as file_100:
        lines = file_100.readlines()

    with open(filename, 'w', encoding="utf-8") as file_100:
        for line in lines:
            file_100.write(line)
            if search_string in line:
                file_100.write(new_string)
