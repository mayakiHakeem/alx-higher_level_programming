#!/usr/bin/python3
# 5-save_to_json_file.py
""" Defines a function that writes an Object to a text file, using JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file
    Args:
        my_obj: obj to write to filename
        filename: file to write my_ob to
    Returns:
        None
    """
    with open(filename, "w", encoding="UTF8") as writer:
        json_rep = json.dumps(my_obj)
        writer.write(json_rep)
