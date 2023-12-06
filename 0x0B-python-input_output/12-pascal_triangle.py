#!/usr/bin/python3
""" 12-pascal_triangle.py """


def pascal_triangle(n):
    """ This function returns a list of integers representing the
        Pascal's triangle """
    if n <= 0:
        return []

    trg = [[1]]
    while len(trg) < n:
        last = trg[-1]
        tmp = [1]
        for i in range(len(last) - 1):
            tmp.append(last[i] + [i + 1])
        tmp.append(1)
        trg.append(tmp)

    return trg
