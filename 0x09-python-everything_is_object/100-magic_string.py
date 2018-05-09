#!/usr/bin/python3
def magic_string():
    magic_string.__dict__.append('Holberton')
    return ', '.join(magic_string.__dict__)
