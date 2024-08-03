#!/usr/bin/python3
"""Modules write to a file at a line after matching search"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file
    """
    with open(filename, "r+", encoding="UTF8") as content:
        line_list = content.readlines()
        content.seek(0)
        content.truncate(0)
        for line in line_list:
            content.write(line)
            if search_string in line:
                content.write(new_string)
