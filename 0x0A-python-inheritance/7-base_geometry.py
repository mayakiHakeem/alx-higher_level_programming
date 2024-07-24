#!/usr/bin/python3
# 5-base_geometry.py
"""Define a geometry module"""


class BaseGeometry():
    """A geometry based class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if value.__class__ != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
