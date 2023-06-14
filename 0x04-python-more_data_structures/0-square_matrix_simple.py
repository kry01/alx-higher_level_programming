#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for arr in matrix:
        new_arr = []
        for i in range(len(arr)):
            new_arr.append(arr[i] * arr[i])
        new_matrix.append(new_arr)
    return new_matrix
