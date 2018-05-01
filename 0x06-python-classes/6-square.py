#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @staticmethod
    def __check_size(size):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @staticmethod
    def __check_position(position):
        if (type(position) != tuple or not
                type(position[0]) == int == type(position[1])
                or len(position) != 2
                or position[0] < 0
                or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        Square.__check_size(value)
        self.__size = value

    @position.setter
    def position(self, value):
        Square.__check_position(value)
        self.__position = value

    def area(self):
        return self.size * self.size

    def my_print(self):
        [print() for y in range(self.position[1])]
        for i in range(self.size):
            [print(' ', end='') for x in range(self.position[0])]
            [print('#', end='') for i in range(self.size)]
            print()
        if self.size == 0:
            print()

if __name__ == '__main__':
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
