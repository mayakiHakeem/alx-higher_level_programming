#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divide corresponding elements in 2 lists of variable length.

    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: length of list to return

    Returns:
        A new list which contains result of dividing corresponding elements.
    """
    new_list = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            res = 0
        except IndexError:
            res = 0
            print("out of range")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        finally:
            new_list.append(res)
    return new_list
