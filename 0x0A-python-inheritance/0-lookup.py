#!/usr/bin/python3
# 0-lookup.py
"""Module that return a list of all attributes and methods of an object"""


def lookup(obj):
    """A function that returns list of methods and attributes
       Args:
       obj: to get method for
       Returns:
       list of methods and attributes available for the class
    """
    return dir(obj)
