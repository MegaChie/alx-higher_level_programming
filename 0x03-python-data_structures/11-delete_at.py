#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list):
        return my_list
    elif idx < 0:
        return my_list
    else:
        list.remove(my_list[idx])
