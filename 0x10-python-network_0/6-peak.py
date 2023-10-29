#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ look for a peak in the given list """
    n = len(list_of_integers)
    tmp = list(list_of_integers)
    if len(tmp) == 0:
        return 0
    else:
        if tmp[0] >= tmp[1]:
            if tmp[0] > tmp[-1]:
                print(tmp[0])
        else:
            for place in range(1, len(tmp)):
                if tmp[place] >= tmp[place + 1]:
                    if tmp[place] > tmp[place - 1]:
                        print(tmp[place])
                else:
                    print(tmp[-1])
