#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    dig = number % 10
    print("{}".format(dig), end='')
    return dig
