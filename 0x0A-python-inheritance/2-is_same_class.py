#!/usr/bin/python3
# 2-is_same_class.py
"""A module that checks object's class"""


def is_same_class(obj, a_class):
    """Check if obj is an exact instance of class a_class

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an exact instance of a_class, False otherwise.
    """
    return type(obj) == a_class
