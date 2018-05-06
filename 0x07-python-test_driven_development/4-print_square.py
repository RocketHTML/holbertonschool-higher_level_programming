#!/usr/bin/python3
"""
.
.
.
.
"""

def print_square(size):
    """
    .
    .
    .

    """
    err_int = 'size must be an integer'
    err_neg = 'size must be >= 0'
    if type(size) != int:
        raise TypeError(err_int)
    if size < 0:
        raise ValueError(err_neg)
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
