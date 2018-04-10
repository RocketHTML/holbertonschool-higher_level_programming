#!/usr/bin/python3
def uppercase(str):
    s = list(str)
    for i in range(len(s)):
        if (ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z')):
            s[i] = chr(ord(s[i]) - (ord('a') - ord('A')))
    print('{}'.format(''.join(s)))
