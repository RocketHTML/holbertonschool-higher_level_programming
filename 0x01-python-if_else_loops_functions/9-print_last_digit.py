#!/usr/bin/python3
def print_last_digit(number):
    digit = int(((number * number) ** (1/2)) % 10)
    print('{}'.format(digit), end='')
    return digit

if __name__ == '__main__':
    print_last_digit(10)
    print_last_digit(11)
    print_last_digit(-10)
    print_last_digit(-11)
