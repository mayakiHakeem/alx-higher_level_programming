#!/usr/bin/python3
"""Class that defines a square"""

class Square():
    """Initialize size of square and calc. area
    Attributes:
       size (int): size to be squared
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        try:
            assert type(size) == int
            self.__size = size
        except AssertionError:
            raise ValueError("size must be an integer")
        
    def area(self):
        return self.__size ** 2
