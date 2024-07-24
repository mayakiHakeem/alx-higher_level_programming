#!/usr/bin/python3
# 5-base_geometry.py
"""Define a geometry module"""


class BaseGeometry():
    """A geometry based class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("age must be an integer")
        if value <= 0:
            raise ValueError("age must be greater than 0")
