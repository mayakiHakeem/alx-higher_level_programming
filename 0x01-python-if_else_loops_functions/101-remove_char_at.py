#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > (len(str) - 1):
        return str
    else:
        return ("{}{}".format(str[0:n],str[n+1:]))
