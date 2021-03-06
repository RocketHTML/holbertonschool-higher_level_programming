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

if __name__ == '__main__':
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
