#!/usr/bin/python3


def uniq_add(my_list=[]):
    if my_list:
        new_list = []
        [new_list.append(x) for x in my_list if x not in new_list]

        result = 0
        for x in new_list:
            result += x
    return result
