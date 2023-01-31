#!/usr/bin/python3.5
""" multiply matrix by matrix. """


import numpy as np
def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices.
    Args: m_a - matrix a
          m_b - matrix b """
    return (np.matmul(m_a, m_b))
