#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    L = len(text)
    i = 0
    while i < L:
        if text[i] in [".", "?", ":"]:
            print(text[i] + "\n")
            if i + 1 < L and text[i + 1] == " ":
                i += 1
        else:
            print(text[i], end='')
        i += 1
