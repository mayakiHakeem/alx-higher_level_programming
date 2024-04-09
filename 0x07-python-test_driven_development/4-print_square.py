#!/usr/bin/python3
""" A function that prints a square with the character #
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
"""


def print_square(size):
    """ A function that print a square
        Args:
            size: size of the square is supplied
    """
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for _ in range(size):
            print('#' * size)
