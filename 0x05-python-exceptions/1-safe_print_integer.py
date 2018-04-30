#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True

if __name__ == '__main__':
    value = None
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "Holberton"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
