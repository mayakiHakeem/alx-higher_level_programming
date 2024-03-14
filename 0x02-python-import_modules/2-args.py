#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    if length < 2:
        print("{} arguments.".format(length - 1))
    elif length == 2:
        print("{} argument.".format(length - 1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments.".format(length - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
