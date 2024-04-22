#!/usr/bin/python3
"""Defines the class Square"""


class Square:
    """Validate the instance attribute
    Attributes:
       size (int): The size of the square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integersize must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
