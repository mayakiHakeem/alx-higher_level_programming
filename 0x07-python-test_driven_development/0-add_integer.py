#!/usr/bin/python3
# add_integer.py
""" defines an integer addition function """


def add_integer(a, b=98):
    """
    Does the integeral addition of  two numbers (integers and float)

    Parameters:
    a (int or float): first num to add
    b (int or float): second num to add

    Returns:
    int: sum of the two numbers

    Raises:
    TypeError: if the number is not int or float

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
