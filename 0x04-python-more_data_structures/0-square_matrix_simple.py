#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for dim in matrix:
        new_matrix += [list(map(lambda x: x**2, dim))]
    return new_matrix
