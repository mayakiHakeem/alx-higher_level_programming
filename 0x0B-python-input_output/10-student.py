#!/usr/bin/python3
# 10-student.py
"""Module define a Student class"""


class Student:
    """Defines a Student object"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            if not attrs:
                return {}

            attrs_dict = {}
            for item in attrs:
                if item in self.__dict__.keys():
                    attrs_dict[item] = self.__dict__[item]
            return attrs_dict
        else:
            return self.__dict__
