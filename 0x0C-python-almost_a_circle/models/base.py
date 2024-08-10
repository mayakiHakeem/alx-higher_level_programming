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
        if list_dictionaries is None:
            return "[]"

        if not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        if not all(isinstance(item, dict) for item in list_dictionaries):
            raise TypeError("list_dictionaries must only contain dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Returns JSON string representation

        Args:
            list_objs (list): list of objs to convert to JSON

        Raises:
            TypeError: list_objs not a list or contain non-obj type element
        """
        if list_objs is None:
            return "[]"

        if not isinstance(list_objs, list):
            raise TypeError("list_objs must be a list")
        if not all([isinstance(item, Base) for item in list_objs]):
            raise TypeError("every item of list_objs must be instances of Base")

        with open(f"{cls.__name__}.json", 'w', encoding="UTF8") as n_file:
            new_list = []
            for item in list_objs:
                it = item.to_dictionary()
                new_list.append(it)
            n_file.write(Base.to_json_string(new_list))
