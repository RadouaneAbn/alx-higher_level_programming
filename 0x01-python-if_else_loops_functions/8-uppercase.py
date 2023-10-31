#!/usr/bin/python3

def islower(c):
    if ord(c) in range(97, 123):
        return True
    return False


def uppercase(str):
    for c in str:
        print("{}".format(chr(ord(c) - 32) if islower(c) else c), end='')
    print()
