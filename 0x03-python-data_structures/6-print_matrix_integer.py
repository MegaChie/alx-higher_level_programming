#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for raw in range(len(matrix)):
            for collumn in range(len(matrix[raw])):
                if collumn != len(matrix[raw]) - 1:
                    space = ' '
                else:
                    space = ''
                print("{:d}".format(matrix[raw][collumn]), end=space)
            print()
