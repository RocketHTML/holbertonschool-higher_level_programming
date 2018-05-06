#!/usr/bin/python3
"""
This module multiplies 2 matrixes
Raises ValueError TypeError
"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrixes
    """
    err_li = (TypeError, '{} must be a list')
    err_lili = (TypeError, '{} must be a list of lists')
    err_empt = (ValueError, "{} can't be empty")
    err_num = (TypeError, "{} should contain only integers or floats")
    err_rec = (TypeError, "each row of {} must should be of the same size")
    err_comp = (ValueError, "m_a and m_b can't be multiplied")

    if type(m_a) != list:
        raise err_li[0](err_li[1].format('m_a'))
    if type(m_b) != list:
        raise err_li[0](err_li[1].format('m_b'))
    if any([type(li) != list for li in m_a]):
        raise err_lili[0](err_lili[1].format('m_a'))
    if any([type(li) != list for li in m_b]):
        raise err_lili[0](err_lili[1].format('m_b'))
    if len(m_a) == 0 or any([len(li) == 0 for li in m_a]):
        raise err_empt[0](err_empt[1].format('m_a'))
    if len(m_b) == 0 or any([len(li) == 0 for li in m_b]):
        raise err_empt[0](err_empt[1].format('m_b'))
    for li in m_a:
        for ele in li:
            if type(ele) != int and type(ele) != float:
                raise err_num[0](err_num[1].format('m_a'))
    for li in m_b:
        for ele in li:
            if type(ele) != int and type(ele) != float:
                raise err_num[0](err_num[1].format('m_b'))
    if any([len(m_a[i]) != len(m_a[0]) for i in range(len(m_a))]):
        raise err_rec[0](err_rec[1].format('m_a'))
    if any([len(m_b[i]) != len(m_b[0]) for i in range(len(m_b))]):
        raise err_rec[0](err_rec[1].format('m_b'))
    if len(m_a[0]) != len(m_b):
        raise err_comp[0](err_comp[1])

    new_m = []
    for row in range(len(m_a)):
        new_m.append([])
        for col in range(len(m_b[0])):
            new_m[row].append(0)

    for r in range(len(new_m)):
        for c in range(len(new_m[r])):
            m_sum = 0
            for col in range(len(m_a[r])):
                m_sum += m_a[r][col] * m_b[col][c]
            new_m[r][c] = m_sum

    return new_m
