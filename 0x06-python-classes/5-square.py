#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @staticmethod
    def __check_size(size):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        Square.__check_size(value)
        self.__size = value

    def area(self):
        return self.size * self.size

    def my_print(self):
        for i in range(self.size):
            [print('#', end='') for i in range(self.size)]
            print()
        if self.size == 0:
            print()

if __name__ == '__main__':
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
