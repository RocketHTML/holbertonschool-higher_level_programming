#!/usr/bin/python3
"""documentation placeholder
    test
    test
    test
"""
from models.base import Base


class Rectangle(Base):
    """documentation
        test
        test
        test
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validate(name, value):
        typmsg = '{} must be an integer'
        negmsg = '{} must be > 0'
        gtemsg = '{} must be >= 0'
        if type(value) != int:
            raise TypeError(typmsg.format(name))
        if name == 'width' or name == 'height':
            if value < 0:
                raise ValueError(negmsg.format(name))
        if name == 'x' or name == 'y':
            if value < 0:
                raise ValueError(gtemsg.format(name))

    def to_dictionary(self):
        attrs = ['id', 'width', 'height', 'x', 'y']
        return self.make_dict(self, attrs)

    @staticmethod
    def attrs():
        return ['id', 'width', 'height', 'x', 'y']

    def update(self, *args, **kwargs):
        attrs = ['id', 'width', 'height', 'x', 'y']
        self.setattrs_from_splat(self, attrs, *args, **kwargs)

    def __str__(self):
        rep = '[Rectangle] ({}) {}/{} - {}/{}'
        i, x, y, w, h = self.id, self.x, self.y, self.width, self.height
        return rep.format(i, x, y, w, h)

    def area(self):
        return self.width * self.height

    def display(self):
        if self.width == 0:
            return
        tags = '#' * self.width
        xspace = ' ' * self.x
        yspace = '\n' * self.y
        print(yspace, end='')
        for i in range(self.height):
            print(xspace + tags)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.validate('width', value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.validate('height', value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        Rectangle.validate('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        Rectangle.validate('y', value)
        self.__y = value
