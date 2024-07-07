#!/usr/bin/python3
# 2-matrix_divided.py
"divides every element of a matrix"


def matrix_divided(matrix, div):
    """
    Divides every number in a matrix

    Parameters:
    matrix (list): a list of lists of integers/floats
    div (float/int): number to divide every number in matrix

    Returns:
    list: the resulting matrix after the division

    Raises:
    TypeError: if div is not a number
               and if matrix is not a list of lists of integers/floats
    ZeroDivisionError: if div is zero
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(sub_list, list) for sub_list in matrix):
        raise TypeError("matrix must be a matrix (list of"
                        " lists) of integers/floats")
    if not all(all(isinstance(item, (float, int))
                   for item in sub_list) for sub_list in matrix):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    if len(matrix[0]) == 0:
        raise TypeError("Each row of the matrix must have the same size")
    if not all(len(sub_list) == len(matrix[0]) for sub_list in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([[round(num / div, 2) for num in sub_list] for sub_list in matrix])
