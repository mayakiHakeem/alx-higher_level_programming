#!/usr/bin/python3
# square.py
"""Defines square class, inherits from Recatangle class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance with an optional ID.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The ID of the rectangle. Defaults to None.
        """
        super().__init__(size, size, x=0, y=0, id=None)
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """Get string of Square obj.

        Returns:
            str_form (str): The string form of the Square ibj.
        """
        return (
            "[Square] ({}) {}/{} - {}"
            .format(self.id, self.x, self.y, self.size)
            )
