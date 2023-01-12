#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mulMatrix = list(matrix)
    if not matrix:
        print()
    for raw in range(len(matrix)):
            for collumn in range(len(matrix[raw])):
                mulMatrix[raw][collumn] = matrix[raw][collumn] ** 2
    return mulMatrix
