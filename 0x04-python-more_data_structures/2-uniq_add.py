#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = set(my_list)
    result = 0
    for x in new_list:
        result += x
    return result
