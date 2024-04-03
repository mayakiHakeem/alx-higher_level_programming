#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Divide 2 integers and print result.

    Args:
        a (int): a
        b (int): b

    Returns:
        result.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
