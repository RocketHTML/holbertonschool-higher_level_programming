#!/usr/bin/python3
def magic_string():
    magic_string.__name__ += ':Holberton'
    return ', '.join(magic_string.__name__.split(':')[1:])
