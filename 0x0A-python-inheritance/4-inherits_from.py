#!/usr/bin/python3
# 4-inherits_from.py
"""A module that check class of an object"""


def inherits_from(obj, a_class):
    """checks if an obj is of a class that inherits directly from a_class

    Args:
        obj: object to check class' inheritance
        a_class: class to check with

    Returns:
        True if object's class inherits directly from a_class; False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
