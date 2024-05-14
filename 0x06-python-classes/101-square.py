#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """A class that defines a square, calc. area of square and print it
    Attributes:
       size (int): size of square
    """
    def __init__(self, size, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integer")
        x, y = value
        if not (isinstance(x, int) and isinstance(y, int)):
            raise TypeError("position must be a tuple of 2 positive integer")
        if x < 0 or y < 0:
            raise Exception("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[0]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[1] + "#" * self.__size)

    def __str__(self):
        string = ""

        if self.__size == 0:
            return string

        for _ in range(self.__position[1]):
            string += '\n'
        for _ in range(self.__size):
            string += " " * self.__position[0] + "#" * self.__size + '\n'

        return string.rstrip('\n')
