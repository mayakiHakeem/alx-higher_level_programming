#!/usr/bin/python3
# 2-append_write.py
"""Module defines function that append content to file"""


def append_write(filename="", text=""):
    """Append text to end of filename
    Args:
        filename: filename to append text to
        text: content to write to filename
    """
    with open(filename, "a", encoding="UTF8") as append:
        return append.write(text)
