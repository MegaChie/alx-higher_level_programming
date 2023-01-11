#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mulMatrix = list(matrix)
    if len(matrix) == 0:
        print()
    for raw in range(len(matrix)):
            for collumn in range(len(matrix[raw])):
                mulMatrix[raw][collumn] = matrix[raw][collumn] ** 2
    return mulMatrix
