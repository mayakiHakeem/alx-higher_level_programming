#!/usr/bin/python3
# 1-write_file.py
"""Module write string to file"""


def write_file(filename="", text=""):
    """Write text to filename
    Args:
        filename: file to write to.
        text: content to write to filename
    """
    with open(filename, "w", encoding="UTF8") as file_writer:
        return file_writer.write(text)
