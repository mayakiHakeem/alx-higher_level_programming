#!/usr/bin/python3
# 6-load_from_json_file.py
"""Defines function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file
    Args:
        fiilename: file to read from
    """
    with open(filename, "r", encoding="UTF8") as reader:
        json_read = reader.read()
        obj = json.loads(json_read)
        return obj
