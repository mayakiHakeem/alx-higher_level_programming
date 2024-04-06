#!/usr/bin/python3


def raise_exception_msg(message=""):
    """ Raises exception message

        Args:
            message: message for exception
    """
    try:
        raise TypeError
    except Exception:
        print(message)
