#!/usr/bin/python3
last = ', '
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8:
            last = '\n'
        print('{}{}'.format(i, j), end=last)
