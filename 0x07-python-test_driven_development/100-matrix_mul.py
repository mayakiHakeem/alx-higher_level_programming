#!/usr/bin/python3
# 100-matrix_mul.py
""" A module that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """A function that mathematically compute the multiplication of 2 matrices

       Args:
       m_a (list): first matrix
       m_b (list): second matrix

       Raises:
       TypeError: if m_a or m_b is not a list of lists
       ValueError: if m_a or m_b doesn't have rows of same size or has
                   members neither int nor float or can't multiply

      Returns:
      list: resulting matrix of the multiplication
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all([isinstance(item, list) for item in m_a]):
        raise TypeError("m_a must be a list of lists")
    elif not all([isinstance(item, list) for item in m_b]):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all([all([isinstance(value, (int, float))
                     for value in items]) for items in m_a]):
        raise TypeError("m_a should contain only integers or floats")
    elif not all([all([isinstance(value, (int, float))
                       for value in items]) for items in m_b]):
        raise TypeError("m_b should contain only integers or floats")

    if not all([len(m_a[0]) == len(item) for item in m_a]):
        raise TypeError("each row of m_a must be of the same size")
    elif not all([len(m_b[0]) == len(item) for item in m_b]):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            cell = 0
            for k in range(len(m_b)):
                cell += m_a[i][k] * m_b[k][j]
            row.append(cell)
        result.append(row)
    return result
