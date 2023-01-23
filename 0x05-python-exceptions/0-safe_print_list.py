#!/usr/bin/python3
    try:
        count = 0
        while count < x:
            print("{}".format(my_list[count]), end='')
            count += 1
        print()
        print("nb_print: {}".format(count))
    except IndexError:
        print()
        print("nb_print: {}".format(count))
