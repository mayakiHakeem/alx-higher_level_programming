#!/usr/bin/python3
""" Module to add two integer operands
    Args:
        a: an integer/float operand
        b: an integer/float operand
    Raise:
        TypeError was raised if operands are neither float nor int.
"""


def add_integer(a, b=98):
    """
       >>> print(add_integer(1, 2))
       3
       >>> print(add_integer(100, -2))
       98
       >>> print(add_integer(2))
       100
       >>> print(add_integer(100.3, -2))
       98
       >>> try:
               print(add_integer(4, "School"))
           except Exception as e:
               print(e)
       b must be an integer
       >>> try:
               print(add_integer(None))
           except Exception as e:
               print(e)
       a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
