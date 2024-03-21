#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    new_dict = {k: v for k, v in a_dictionary.items() if k != key}
    return new_dict
