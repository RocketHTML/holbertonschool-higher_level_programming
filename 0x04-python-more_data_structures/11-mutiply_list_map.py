#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    x = lambda y: y * number
    return list(map(x, my_list))
