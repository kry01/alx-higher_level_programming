#!/bin/usr/python3
"""
"""


def matrix_divided(matrix, div):
    if type(matrix) is not list and not all((type(row) is list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not all((len(row) == matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for i in matrix:
            for j in matrix[i]:
                