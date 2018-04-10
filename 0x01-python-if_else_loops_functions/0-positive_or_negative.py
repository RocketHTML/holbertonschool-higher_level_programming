#!/usr/bin/python3
import random
number = random.randint(-10, 10)
string = "is zero"
if number > 0:
    string = "is positive"
if number < 0:
    string = "is negative"
print('{} {}'.format(number, string))
