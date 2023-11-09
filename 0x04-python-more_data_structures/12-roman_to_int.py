#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    if type(roman_string) is not str or roman_string is None:
        return value

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    less = {'IV': 4, 'IX': 9, 'XC': 90, 'CM': 900}
    i = 0
    while i < len(roman_string):
        if roman_string[i:i + 2] in less:
            value += less[roman_string[i:i + 2]]
            i = i + 1
        else:
            value += roman.get(roman_string[i], 0)
        i = i + 1
    return value
