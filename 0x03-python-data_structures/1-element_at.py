#!/usr/bin/python3
def element_at(my_list, idx):
    count = int(idx)
    if count < 0:
        return None
    elif count >= len(my_list):
        return None
    else:
        return my_list[count]
