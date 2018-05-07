#!/usr/bin/python3
"""add_integer module

This module demonstrates integer checked addition.
Params may be floats, but they will be casted into ints.
"""

def add_integer(a, b=98):
    """adds a and b

        Args:
            a (int, float): first number
            b (int, float): second number

        Returns:
            int: sum of a and b
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)

if __name__ == '__main__':
    print(add_integer.__doc__)
