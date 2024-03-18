#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for sub_mat in matrix:
        for num in sub_mat:
            if num != sub_mat[-1]:
                print("{} ".format(num), end='')
            else:
                print("{}".format(num), end='')
        print()
