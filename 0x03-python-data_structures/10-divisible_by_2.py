#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divList = []
    for place in my_list:
        if place % 2 == 0:
            divList.append(True)
        else:
            divList.append(False)
    return divList
