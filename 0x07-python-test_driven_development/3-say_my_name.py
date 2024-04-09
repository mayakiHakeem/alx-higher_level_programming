#!/usr/bin/python3
"""
    A function that prints first_name and last_name
    Exception:
        raised TypeError if first or last_name is not string
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    >>> try:
    ...     say_my_name(12, "White")
    ... except Exception as e:
    ...     print(e)
    first_name must be a string
"""


def say_my_name(first_name, last_name=""):
    """ A function that concatenate two string together
        Args:
            first_name: user first name
            last_name: user last name
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print('My name is {} {}'.format(first_name, last_name))
