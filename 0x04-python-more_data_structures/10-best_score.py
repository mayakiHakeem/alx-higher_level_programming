#!/usr/bin/python3


def best_score(a_dictionary):
    best_score = 0
    best_student = ''
    if a_dictionary:
        for k,  v in a_dictionary.items():
            if v > best_score:
                best_score = v

        for k, v in a_dictionary.items():
            if v == best_score:
                return k
    return None
