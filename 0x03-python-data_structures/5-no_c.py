#!/usr/bin/python3
def no_c(my_string):
    holder = list(my_string)
    place = 0
    for count in holder:
        if count == 'c' or count == 'C':
            holder[place] = ""
        place += 1
    return "".join(holder)
