#!/usr/bin/python3
# 1-my_list.py
"""A module of class that inherit from list"""


class MyList(list):
    """A class that inherit from list to print sorted list"""

    def print_sorted(self):
        """print the list to stdout sorted in ascending order
        Args:
           self (MyList): instance of MyList
        Returns:
           None
        """
        print(sorted(self))
