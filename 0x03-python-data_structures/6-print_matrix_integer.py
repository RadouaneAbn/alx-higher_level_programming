#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        L = len(matrix[i])
        for j in range(L):
            print("{:d}".format(matrix[i][j]), end='')
            print("{}".format(' ' if j < L - 1 else ''), end='')
        print()
