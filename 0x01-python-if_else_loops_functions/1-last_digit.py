#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = int(((number * number) ** (1/2)) % 10)
if number < 0:
    digit *= -1
string = "and is 0"
if digit > 5:
    string = "and is greater than 5"
if digit < 6 and digit != 0:
    string = "and is less than 6 and not 0"
print('Last digit of {} is {:.0f} {}'.format(number, digit, string))
