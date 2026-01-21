#!/usr/bin/python3
"""
Module: 0-square_matrix_simple
Contains a function that computes the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    """
    Returns a new matrix where each value is the square of the value
    of the input matrix.

    Args:
        matrix (list of lists): 2D array of integers

    Returns:
        list of lists: new 2D array with squared values
    """
    return [[value * value for value in row] for row in matrix]
