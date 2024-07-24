#!/usr/bin/python3
# 10-square.py
"""Module that define a square class off a rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that defines a square"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        return self.__size ** 2
