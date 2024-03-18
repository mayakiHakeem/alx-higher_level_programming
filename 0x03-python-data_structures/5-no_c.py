#!/usr/bin/python3


def no_c(my_string):
    ctring = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        else:
            ctring += char
    return ctring
