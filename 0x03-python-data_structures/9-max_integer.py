#!/usr/bin/python3
def max_integer(my_list=[]):
    m = None
    for x in my_list:
        if m is None or m < x:
            m = x
    return m

if __name__ == '__main__':
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    negatives = [-1, -2, -3, -4]
    max_value = max_integer(my_list)
    empty = max_integer()
    nega = max_integer(negatives)
    print("Max: {}".format(max_value))
    print("Empty: {}".format(empty))
    print("Negative Max: {}".format(nega))
