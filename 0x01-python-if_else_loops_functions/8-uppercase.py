#!/usr/bin/python3
def uppercase(str):
    for place in str:
        place = ord(place)
        if 97 <= place <= 122:
            place = place - 32
        print("{}".format(chr(place)), end='')
    print()
