#!/usr/bin/python3
from time import sleep
size = 62
helix1 = 0
helix2 = 61
delta = 1
weight = 3 - (abs((15 - helix1)) // 5) 
bounce = 0
while(bounce < 200):
    sleep(0.04)
    i = 0
    while(i < 62):
        if (i == helix1 or i == helix2):
            print('$$', end='')
        else:
            print(' ', end='')
        i += 1
    weight = 3 - (abs((15 - helix1)) // 5)
    helix1 += delta + (weight * delta)
    helix2 -= delta + (weight * delta)
    #print(' helix1: {}'.format(helix1), end='')
    #print(' helix2: {}'.format(helix2), end='')
    #print(' bounce: {}'.format(bounce), end='')
    #print(' delta: {}'.format(delta), end='')
    #print(' weight: {}'.format(weight * delta), end='')
    print('')
    if helix1 > helix2 or helix1 + (weight * delta) <= 0:
        delta *= -1
        bounce += 1
