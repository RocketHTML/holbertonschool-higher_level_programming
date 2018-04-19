#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    if type(my_list) != list:
        return total
    cln = my_list[:]
    cln.sort()
    for i in range(len(cln)):
        v = i - 1
        if cln[i] != cln[v]:
            total += cln[i]
    return total

if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
