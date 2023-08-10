#!/usr/bin/python3
""" This file contain matrix_devided function
"""


def matrix_divided(matrix, div):
    """ matrix_devided function thats devide the whole matrix by div number
    """
    if (type(matrix) is not list or
            not all((type(row) is list) for row in matrix)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    elif not all((len(row) == len(matrix[0])) for row in matrix):
        raise TypeError("Each row of the matrix must"
                        " have the same size")

    elif type(div) not in [int, float]:
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    else:
        return ([list(map(lambda x: round(x / div, 2), row))
                for row in matrix])
