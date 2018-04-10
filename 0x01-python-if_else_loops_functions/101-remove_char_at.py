#!/usr/bin/python3
def remove_char_at(str, n):
    s = list(str)
    if (n < 0 or n > len(str) - 1):
        return str
    s.pop(n)
    return(''.join(s))

if __name__ == '__main__':
    print(remove_char_at("Holberton School", 3))
    print(remove_char_at("Chicago", 2))
    print(remove_char_at("C is fun!", 0))
    print(remove_char_at("School", 10))
    print(remove_char_at("Python", -2))
