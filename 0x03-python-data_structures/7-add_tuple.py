#!/usr/bin/python3
    if len(tuple_a) > 2:
        tuple_a = tuple_a[:2]
    elif len(tuple_a) == 1:
        tuple_a += (0,)
    elif len(tuple_a) == 0:
        tuple_a += (0,0)
    if len(tuple_b) > 2:
        tuple_b = tuple_a[:2]
    elif len(tuple_b) == 1:
        tuple_b += (0,)
    elif len(tuple_b) == 0:
        tuple_b += (0,0)
    result = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return result
