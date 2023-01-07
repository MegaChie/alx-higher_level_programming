#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    elif:
        for raw in range(len(matrix)):
            for collumn in range(len(matrix[raw])):
                if collumn != len(matrix[raw]) - 1:
                    space = ' '
                else:
                    space = ''
                print("{}".format(matrix[raw][collumn]), end=space)
            print()
