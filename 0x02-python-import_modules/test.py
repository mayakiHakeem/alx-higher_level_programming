#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    length = len(sys.argv)

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, *, /")
    sys.exit(1)

    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
                                                                                            
