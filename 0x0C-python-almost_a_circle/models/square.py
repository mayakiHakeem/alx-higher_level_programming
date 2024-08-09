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
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return string of Square obj.

        Returns:
            str_form (str): The string form of the Square ibj.
        """
        return (
            "[Square] ({}) {}/{} - {}"
            .format(self.id, self.x, self.y, self.size)
            )

    @property
    def size(self):
        """Get value of the size of Square obj.

        Returns:
            (int): value of the Square obj.
        """
        return self.__width

    @size.setter
    def size(self, value):
        """Set value of the size of Square obj.

        Args:
            value (int): new value of the Square obj size.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is not > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Update the attr of the Square object.

        Args:
            *args: Non-keyword arguments to update attributes in order
            **kwargs: Keyword arguments to update attributes by name
        Raises:
            TypeError: if number of args is greater than 5
        """
        if len(args) > 4:
            raise TypeError()

        attrs = ['id', 'size', 'x', 'y']

        for attr, value in zip(attrs, args):
            setattr(self, attr, value)

        for key, value in kwargs.items():
            if key not in attrs[:len(args)]:
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square obj.

        Returns:
            dict_rep (dict): dictionary rep of obj
        """
        attrs = ['id', 'size', 'x', 'y']
        dict_rep = {}

        for item in attrs:
            attr = getattr(self, item)
            dict_rep[item] = attr
        return dict_rep
