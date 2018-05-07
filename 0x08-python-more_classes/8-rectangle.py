#!/usr/bin/python3
"""Rectangle Module

This module defines a rectangle

Example:
    >>> x = Rectangle()

"""


class Rectangle:
    """Defines a Rectangle object

    This class provides methods to define and print
    Rectangle objects, and it also keeps track
    of the Rectangles instantiated. You can change the
    print_symbol for the class to any type,
    and you can instantiate a square Rectangle.

    Attributes:
        number_of_instances (int): total number of rects
        print_symbol (optional): defines a rect's string rep
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor function for Rectangles.

            The number_of_instances class attribute is incremented by 1
            whenever __init__ method is called.

            Args:
                width (int): width of rectangle
                height (int): height of rectangle

            Raises:
                TypeError: If width or height are not ints
                ValueError: If width or height are < 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns private __width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets private __width attribute

            Args:
                value(int): value to set width to

            Raises:
                TypeError: If width is not int
                ValueError: If width is < 0
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """returns private __height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets private __height attribute

            Args:
                value(int): value to set height to

            Raises:
                TypeError: If height is not int
                ValueError: If height is < 0
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def area(self):
        return self.width * self.height

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def __ge__(self, rect_2):
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if self.area() >= rect_2.area():
            return True
        else:
            return False

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1 >= rect_2:
            return rect_1
        else:
            return rect_2

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        ret = [str(self.print_symbol) * self.width + '\n'
               for i in range(self.height)]
        return ''.join(ret)

    def __repr__(self):
        rep = 'Rectangle({}, {})'.format(self.width, self.height)
        return rep


if __name__ == '__main__':
    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(
            my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")
