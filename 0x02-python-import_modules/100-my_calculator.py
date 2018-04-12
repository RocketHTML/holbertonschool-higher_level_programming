#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    ops = ['+', '-', '*', '/']
    funcs = [add, sub, mul, div]
    choice = None

    for i in range(len(ops)):
        if argv[2] == ops[i]:
            choice = i
    if choice is None:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print('{} {} {} = {}'.format(a, ops[choice], b, funcs[choice](a, b)))
