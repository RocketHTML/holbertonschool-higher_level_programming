#!/usr/bin/python3
"""
.
.
.
.
"""

def say_my_name(first_name, last_name=""):
    """.
        .
            .
    """
    err_fir = 'first_name must be a string'
    err_las = 'last_name must be a string'
    msg = 'My name is {} {}'
    if type(first_name) != str:
        raise TypeError(err_fir)
    elif type(last_name) != str:
        raise TypeError(err_las)
    print(msg.format(first_name, last_name))
