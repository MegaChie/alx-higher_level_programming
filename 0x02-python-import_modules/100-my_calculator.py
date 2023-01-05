#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import sub, add, div, mul
    agumentVector = sys.argv[1:]
    argumentCount = len(agumentVector)
    operator = ["+", "-", "*", "/"]
    if argumentCount != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
        elif sys.argv[2] == "*":
            print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
        elif sys.argv[2] == "-":
            print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
        elif sys.argv[2] == "/":
            print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
