#!/usr/bin/python3
"""
    A Module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
        A function that divides all elements of a matrix
        Raises:
            TypeErrors: if matrix and element in matrix not a number
            ZeroDvisionError: if div is equal to zero exception raise
    """
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    elif len(matrix[0]) == 0:
        raise TypeError('Each row of the matrix must have the same size')
    elif not all(len(rows) == len(matrix[0]) for rows in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    elif not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    else:
        return [[round(num / div, 2) for num in row] for row in matrix]
