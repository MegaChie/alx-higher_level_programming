#!/usr/bin/python3
for count in range(122, 96, -1):
    if count % 2 == 1:
        count -= 32
    print("{}".format(chr(count)), end="")
