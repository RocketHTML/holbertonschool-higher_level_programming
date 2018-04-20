#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for keys, values in a_dictionary.items():
        if values == value:
            del a_dictionary[key]
