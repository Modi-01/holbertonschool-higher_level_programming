#!/usr/bin/python3
"""
6-print_matrix_integer
"""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, one row per line."""
    for row in matrix:
        for j in range(len(row)):
            if j != len(row) - 1:
                print("{:d}".format(row[j]), end=" ")
            else:
                print("{:d}".format(row[j]), end="")
        print()
