#!/usr/bin/python3


def matrix_divided(matrix, div):
    err_list = 'matrix must be a matrix (list of lists) of integers/floats'
    err_size = 'Each row of the matrix must have the same size'
    err_divnum = 'div must be a number'
    err_divzero = 'division by zero'
    if (type(matrix) != list or
            any([type(matrix[i]) != list for i in range(len(matrix))])):
        raise TypeError(err_list)
    if not (type(div) in [int, float]):
        raise TypeError(err_divnum)
    if div == 0:
        raise ZeroDivisionError(err_divzero)
    size = len(matrix)
    if size == 0:
        raise TypeError(err_list)
    size = len(matrix[0])
    i = 0
    new_matrix = []
    for li in matrix:
        if (len(li) != size):
            raise TypeError(err_size)
        new_matrix.append([])
        for ele in li:
            if not (isinstance(ele, int) or isinstance(ele, float)):
                raise TypeError(err_list)
            new_matrix[i].append(float('{:.2f}'.format(float(ele) / float(div))))
        i += 1
    
    return new_matrix
