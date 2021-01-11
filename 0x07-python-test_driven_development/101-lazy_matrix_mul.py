#!/usr/bin/python3
"""Module with function that multiplies two matrices using NumPy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrices"""
    return numpy.matmul(m_a, m_b)
