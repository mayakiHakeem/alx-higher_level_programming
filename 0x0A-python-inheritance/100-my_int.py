#!/usr/bin/python3
# 100-my_int.py
"""Module that define a special int class off a int"""
Rectangle = __import__('9-rectangle').Rectangle


class MyInt(int):
    """class that defines MyInt"""

    def __eq__(self, other):
        """check for equality of 2 objects
        Args:
            self (int):
            other (int):
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """check for inequality of 2 objects
        Args:
            self (int):
            other (int):
        """
        return not super().__ne__(other)
