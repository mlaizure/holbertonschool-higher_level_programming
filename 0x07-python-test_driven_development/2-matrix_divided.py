#!/usr/bin/python3
"""Module has a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix which must be ints or floats
    by a number (div) rounded to 2 decimal places"""
    e_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(e_msg)
    row_len = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(e_msg)
        row_len.append(len(row))
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError(e_msg)
    if len(set(row_len)) > 1:
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    result = [[round(element/div, 2) for element in row]for row in matrix]
    return result
