#!/usr/bin/python3
def fizzbuzz():
    for i in range (1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            to_print = 'FizzBuzz'
        elif (i % 3 == 0):
            to_print = 'Fizz'
        elif (i % 5 == 0):
            to_print = 'Buzz'
        else:
            to_print = i
        print('{}'.format(to_print), end=' ')

if __name__ == '__main__':
    fizzbuzz()
    print("")
