#!/usr/bin/python3
# base.py
"""Module defines the Base class"""
import json
import csv


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
        """Write JSON of list_objs to file

        Args:
            list_objs (list): list of objs to convert to JSON

        Raises:
            TypeError: list_objs not a list or contain non-obj type element
        """
        if list_objs is None or len(list_objs) == 0:
            with open(f"{cls.__name__}.json", 'w', encoding="UTF8") as n_file:
                n_file.write("[]")
            return

        if not isinstance(list_objs, list):
            raise TypeError("list_objs must be a list")
        if not all([isinstance(item, Base) for item in list_objs]):
            raise TypeError("all item of list_objs must be instances of Base")

        flag = list_objs[0].__class__.__name__
        for i in range(1, len(list_objs)):
            if flag != list_objs[i].__class__.__name__:
                raise TypeError()

        with open(f"{cls.__name__}.json", 'w', encoding="UTF8") as n_file:
            new_list = []
            for item in list_objs:
                it = item.to_dictionary()
                new_list.append(it)
            n_file.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns data from JSON string repr.

        Args:
            json_string (json): json string object to convert

        Returns:
            data: data repr with json str

        Raises:
            TypeError: if json_string not json obj
        """
        if not json_string:
            return []
        try:
            return list(json.loads(json_string))
        except json.JSONDecodeError:
            raise TypeError("Invalid JSON string")

    @classmethod
    def create(cls, **dictionary):
        """Returns a dummy instance with all attributes already set

        Args:
            dictionary (dict): kwargs

        Returns:
            dummy_instance:
        """
        if not isinstance(dictionary, dict):
            raise TypeError("dictionary must be an instance of dict")

        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(2, 3)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(2)

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return list of instances loaded JSON file

        Raises:
            TypeError: list_objs not a list or contain non-obj type element
        """
        try:
            with open(f'{cls.__name__}.json', 'r') as file:
                content = file.read()
        except FileNotFoundError as e:
            return []

        list_dict = cls.from_json_string(content)

        list_instances = [cls.create(**dictionary) for dictionary in list_dict]

        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
