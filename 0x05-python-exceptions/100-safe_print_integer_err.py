#!/usr/bin/python3


def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as ex:
        sys.stderr.write('Exception: {}\n'.format(ex))
        return False
    else:
        return True

if __name__ == '__main__':
    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "Holberton"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
