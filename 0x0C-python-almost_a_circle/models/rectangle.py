#!/usr/bin/python3
# rectangle.py
"""Defines the rectangle class inheriting from base"""
from models.base import Base

class Rectangle(Base):
    """Initialize a new rectangle instance with an optional ID."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
