#!/usr/bin/python3
def max_integer(my_list=[]):
	count = 0
    if len(my_list) == 0:
        return None
    else:
        my_list.sort()
        return my_list[-1]
