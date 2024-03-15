#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    length = len(sys.argv)
    result = 0
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        if sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif sys.argv[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            
        
