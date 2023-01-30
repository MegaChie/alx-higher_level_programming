#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argumentVector = sys.argv[1:]
    argumentCount = len(argumentVector)
    n = sys.argv[1]
    if type(n) is not int:
        print("N must be a number")
    if n < 4:
        print("N must be at least 4")
        exit(1)
    pass
