#!/usr/bin/python3
# 4-print_square.py
"""print square of length size using '#'"""


def print_square(size):
    """
    Print square of length size with '#'

    Args:
    size (int): length of the square

    Returns:
    None

    Raises:
    TypeError: size must be an integer
    ValueError: size must be >= 0
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
