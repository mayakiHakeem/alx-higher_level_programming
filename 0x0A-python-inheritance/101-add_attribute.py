#!/usr/bin/python3
# 101-add_attribute.py
"""Module define a function that add new attribute to object"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute should be added.
        attr_name: The name of the attribute to add.
        attr_value: The value of the attribute to add.
    Raises:
        TypeError: if the object cannot have new attributes.
    """
    # Check if the object can have new attributes by setting one
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    # If possible, set the attribute
    setattr(obj, attr_name, attr_value)
