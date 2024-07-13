#!/usr/bin/python3
"""
   This module contains a function that indent text.
"""


def text_indentation(text):
    """A function that indent a text

       Args:
       text (str): text to indent

       Exceptions:
       TypeError: if text is not a string

       Returns:
       None
    """
    delim = [':', '.', '?']
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    for i in range(c, len(text)):
        if text[i] in delim:
            print(text[i] + "\n")
        elif text[i - 1] in delim and text[i] == " ":
            continue
        else:
            print(text[i], end='')
