#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            if nb_lines == 1:
                break
            nb_lines -= 1
