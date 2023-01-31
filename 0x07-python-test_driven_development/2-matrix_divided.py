##!/usr/bin/python3
"""  divides elements of matrix by a given number """


def matrix_divided(matrix, div):
    """  divides element of matrix by a number.
    check is matrix is list of lists, elements are numbers,
    second order lists are of the same size. """
    result = []
    text1 = "matrix must be a matrix (list of lists) of integers/floats"
    text2 = "Each row of the matrix must have the same size"
    text3 = "div must be a number"
    text4 = "division by zero"
    if div == 0:
        raise ZeroDivisionError(text4)
    if not isinstance(div, (int, float)):
        raise TypeError(text3)
    for raw in matrix:
        if len(raw) != len(matrix[0]):
            raise TypeError(text2)
        divResult = []
        for element in raw:
            if not isinstance(element, (int, float)):
                raise TypeError(text1)
            else:
                divResult.append(round(element / div, 2))
        result.append(divResult)
    return result
