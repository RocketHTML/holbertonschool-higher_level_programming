#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == ' ' and ((i == 0 or text[i - 1] in "\n.:?") or
        (i == len(text) - 1 or text[i + 1] == '\n')):
                continue
        print(text[i], end='')
        if text[i] in {'.', '?', ':'}:
            print('\n')
