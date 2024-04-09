#!/usr/bin/python3
""" A helper module that validate list items
    Args:
        matrix: list item supplied for validation
        name: name of the operand that contain the items
    Raises:
        TypeError:
            if matrices is not a lists of a list
            if matrices contain anything other than integers
            if row of a matrice is not thesame size
        ValueError:
            if any of the matrices are empty
    Return True if no exception was handled
"""


def matrix_validation(matrix, name):
    if not (isinstance(matrix, list) and all(isinstance(row, list)\
            for row in matrix)):
        raise TypeError('{} must be a list of lists'.format(name))
    elif not (len(matrix) == 0  or all(len(row) for row in matrix)):
        raise ValueError("{} can't be empty".format(name))
    elif not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError('{} should contain only integers or floats'.\
                format(name))
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('each row of {} must be of the same size'.format(name))
    else:
        return True



""" A module that find the product of two matrices
    args:
        m_a: list of integers
        m_b: list of integers
    Raises:
        TypeError:
            from matrix_validation
        ValueError:
            if m_a and m_b can't be multiplied
"""


def matrix_mul(m_a, m_b):
    """
    >>> print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    [[7, 10], [15, 22]]
    >>> print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
    [[13, 16]]
    >>> try:
            print(matrix_mul([[2, 4, 6], [8, 6, 4]], [[]]))
        except Exception as e:
            print(e)
    m_b can't be empty
    >>> try:
            print(matrix_mul([(1, 2, 4), (2, 4, 5)], [(3, 4, 5), (3, 5, 6)]))
        except Exception as e:
            print(e)
    m_a must be a list of lists
    """
    if (matrix_validation(m_a, 'm_a') and matrix_validation(m_b, 'm_b')) == True:
        x_val = []
        m_b_size = len(m_b[0])
        for row in m_a:
            i, j, x = 0, 0, []
            for _ in range(len(row)):
                x_mat = 0
                for index, num in enumerate(row):
                    x_mat += int(num) * int(m_b[i][j])
                    if i == m_b_size - 1:
                        i = 0
                    elif index > m_b_size - 1:
                        raise ValueError("m_a and m_b can't be multiplied")
                    else:
                        i += 1
                x.append(x_mat)
                j += 1
            x_val.append(x)
        return x_val
