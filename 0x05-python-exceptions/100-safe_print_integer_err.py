#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """print argument

        Args:
            value: argument to print

        Returns:
            True if value is int otherwise False
    """
    try:
        print("{:d}".format(value))
    except Exception:
        print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
        return False
    else:
        return True
