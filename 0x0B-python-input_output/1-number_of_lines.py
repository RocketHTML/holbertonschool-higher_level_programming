#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, mode='r', encoding='utf-8') as f:
        count = 0
        for i in f:
            count += 1
        return count
