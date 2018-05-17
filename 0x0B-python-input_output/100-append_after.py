#!/usr/bin/python3


def append_after(filename="",
                 search_string="",
                 new_string=""):
    L = []
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            L.append(line)
            if search_string in line:
                L.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in L:
            print(line, file=f, end='')

if __name__ == '__main__':
    append_after('t.txt', 'pie', 'found you')
