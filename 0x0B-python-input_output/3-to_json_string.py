#!/usr/bin/python3
# 3-to_json_string.py
"""Module defines a function that returns the JSON rep of an object(string)"""
import json


def to_json_string(my_obj):
    """Returns JSON rep of an object
    Args:
        my_obj: object to get JSON rep of.
    Returns:
        JSON representation of my_obj
    """
    return json.dumps(my_obj)
