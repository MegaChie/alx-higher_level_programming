#!/usr/bin/python3
def uppercase(str):
    for count in range(len(str)):
        if(str[count] >= 'a' and str[count] <= 'z'):
            tsm1 = tsm1 + chr((ord(str[count]) - 32))
            print("{}".format(ord(tsm1)))
    else:
        tsm1 = tsm1 + str[count]
        print("{}".format(ord(tsm1)))
