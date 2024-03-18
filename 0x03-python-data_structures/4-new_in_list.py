#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    a_list = my_list{::}
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    a_list[idx] = element
    return a_list
