#!/usr/bin/python3
"""Module with function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    row_len_ma = []
    for row in m_a:
        row_len_ma.append(len(row))
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    row_len_mb = []
    for row in m_b:
        row_len_mb.append(len(row))
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if len(set(row_len_ma)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(row_len_mb)) > 1:
        raise TypeError("each row of m_b must be of the same size")
    if row_len_ma[0] != len(row_len_mb) and row_len_mb[0] != len(row_len_ma):
        raise ValueError("m_a and m_b can't be multiplied")
    product = [[sum(a*b for a, b in zip(ma_row, mb_col))
                for mb_col in zip(*m_b)] for ma_row in m_a]
    return product
