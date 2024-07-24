#!/usr/bin/python3
# 8-rectangle.py
"""A Module that defines a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """class constructor
        Args:
            width (int): positive integer width of rectangle
            height (int): positive integer height of rectangle
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
