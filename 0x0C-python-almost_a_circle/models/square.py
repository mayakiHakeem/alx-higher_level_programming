#!/usr/bin/python3
# square.py
"""Defines square class, inherits from Recatangle class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=0, y=0, id=None)
        self.size = size
        self.x = x
        self.y = y

    
