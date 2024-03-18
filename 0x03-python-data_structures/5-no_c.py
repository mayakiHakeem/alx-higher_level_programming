#!/usr/bin/python3


def no_c(my_string):
    ctring = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            ctring += char
    return ctring
