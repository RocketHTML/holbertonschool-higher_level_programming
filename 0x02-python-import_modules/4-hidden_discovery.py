#!/usr/bin/python3
from hidden_4 import *

if __name__ == '__main__':
    _names = []
    for name in dir():
        if name[0] != '_':
            _names.append(name)
    _names.sort()
    for name in _names:
        print(name)
