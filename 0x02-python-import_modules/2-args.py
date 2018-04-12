#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argc = len(argv)
    string = 'arguments'
    punc = ':'
    if (argc - 1 == 0):
        punc = '.'
    if (argc - 1 == 1):
        string = 'argument'
    to_print = '{} {}{}'.format(argc - 1, string, punc)
    print(to_print)

    for i in range(1, argc):
        print('{}: {}'.format(i, argv[i]))
