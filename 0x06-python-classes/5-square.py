#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """ Square calc. square of size and print with #
    Attributes:
        size (int): size to be squared
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for height in range(self.__size):
                print("#" * self.__size)
