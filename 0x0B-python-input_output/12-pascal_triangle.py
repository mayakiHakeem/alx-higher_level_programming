#!/usr/bin/python3
# 12-pascal_triangle.py
"""Module defines a Pascal-Triangle fxn"""


def pascal_triangle(n):
    """Return Pascal Triangle
    """
    if n == 0:
        return []

    pt = [[1]]
    for row_index in range(2, n+1):
        prev_row = pt[-1]
        lent = len(prev_row)
        pt_row = []
        for col_index in range(lent + 1):
            if col_index == 0 or col_index == lent:
                pt_row.append(1)
            else:
                pt_row.append(prev_row[col_index] + prev_row[col_index - 1])
        pt.append(pt_row)
    return (pt)
