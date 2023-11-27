#!/usr/bin/python3
"""
Queens module

This module solves the N-Queens problem.

Usage:
    ./nqueens.py 6 # prints all solutions.
"""


from sys import argv

if __name__ == "__main__":
    a = []

    # Check command-line arguments
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    # Check if the argument is a valid integer
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)

    # Check if N is at least 4 for a meaningful solution
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the answer list
    for i in range(n):
        a.append([i, None])

    def exist(y):
        """
        Check if a queen already exists.
        """
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def valid(x, y):
        """
        Check if placing a queen at a given position is valid.
        """
        if (exist(y)):
            return False
        i = 0
        while (i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """
        Clear the positions after the current row.
        """
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """
        Recursive function to solve the N-Queens problem.
        """
        for y in range(n):
            clear_a(x)
            if valid(x, y):
                a[x][1] = y
                if (x == n - 1):
                    print(a)
                else:
                    nqueens(x + 1)

    nqueens(0)
