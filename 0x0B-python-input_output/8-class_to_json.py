#!/usr/bin/python3
# 8-class_to_json.py
"""Module defines a clas-to-JSON function"""


def class_to_json(obj):
    """Returns a dict for JSON serialization
    """
    return obj.__dict__
