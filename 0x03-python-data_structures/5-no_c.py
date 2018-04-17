#!/usr/bin/python3
def no_c(my_string):
    res = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            res += c
    return res

if __name__ == '__main__':
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
