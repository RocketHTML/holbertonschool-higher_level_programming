#!/usr/bin/python3

if __name__ == '__main__':
    from hidden_4 import *
    _names = []
    for name in dir():
        if name[0] != '_':
            _names.append(name)
    _names.sort()
    for name in _names:
        print(name)
