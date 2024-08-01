#!/usr/bin/python3
# 0-read_file.py
"""Module that read a file"""


def read_file(filename=""):
    """Read file in from filename

    Args:
        filename: file to read
    """
    with open(filename, "r", encoding="UTF8") as file_reader:
        content = file_reader.read()
        print(content, end="")
