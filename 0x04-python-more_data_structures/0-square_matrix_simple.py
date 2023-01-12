#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        print()
    return [[item**2 for item in row] for row in matrix]
