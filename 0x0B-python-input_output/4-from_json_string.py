#!/usr/bin/python3
# 4-from_json_string.py
"""Defines function that returns object represented by JSON"""
import json


def from_json_string(my_str):
    """Returns an object rep by JSON string
    Args:
        my_str: json string repping a python obj
    Returns:
        python object
    """
    return json.loads(my_str)
