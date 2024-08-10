#!/usr/bin/python3
# base.py
"""Module defines the Base class"""
import json


class Base:
    """Define a Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance with an optional ID.

        Args:
            id (int, optional): The ID of Base object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation

        Args:
            list_dictionaries (list): list of dictionaries to convert to JSON

        Returns:
            json_str: string representation of list_dictionaries

        Raises:
            TypeError: list_dictionaries not a list or contain non-dict element
        """
        if not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        if not all(isinstance(item, dict) for item in list_dictionaries):
            raise TypeError("list_dictionaries must only contain dictionaries")
        return json.dumps(list_dictionaries)
