#!/usr/bin/python3
last = ', '
for i in range(100):
    if i == 99:
        last = '\n'
    print('{:02d}'.format(i), end=last)
