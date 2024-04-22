#!/usr/bin/python3
"""
    A function that prints a text with 2 new lines after each of these
    characters: fullstop, question mark and colon.

    Exceptions:
        TypeError: if file is not a string type
"""


def text_indentation(text):
    """ A function that indent a text """
    delim = [':', '.', '?']
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if text[i] in delim:
            print(text[i] + "\n")
        elif text[i - 1] in delim and text[i] == " ":
            continue
        else:
            print(text[i], end='')
