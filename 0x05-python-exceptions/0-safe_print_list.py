#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except Exception:
        pass
    print()
    return count
