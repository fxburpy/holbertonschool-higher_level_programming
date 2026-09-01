#!/usr/bin/python3
"""Provide a function that divides every element of a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix whose elements are divided by ``div``."""
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(message)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(message)
    if not matrix[0]:
        raise TypeError(message)
    if not all(all(type(item) in (int, float) for item in row)
               for row in matrix):
        raise TypeError(message)
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
