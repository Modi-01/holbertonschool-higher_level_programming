#!/usr/bin/python3
"""Module that provides a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div and round results to 2 decimals."""
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_row = "Each row of the matrix must have the same size"

    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) or row == [] for row in matrix)):
        raise TypeError(err_matrix)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(err_row)
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(err_matrix)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
