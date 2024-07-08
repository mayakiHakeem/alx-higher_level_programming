#!/usr/bin/python3
# 3-say_my_name.py
"""A function that join and print fullname"""


def say_my_name(first_name, last_name=""):
    """
    join and print full_name

    Args:
    first_name (str): first name to be written
    last_name (str): last_name to be written

    Returns:
    None

    Raises:
    TypeError: first_name must be a string
    TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name + " " + last_name)
