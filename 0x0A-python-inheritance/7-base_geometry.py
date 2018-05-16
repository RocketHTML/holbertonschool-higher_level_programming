#!/usr/bin/python3


class BaseGeometry:
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        type_err = '{} must be an integer'.format(name)
        val_err = '{} must be greater than 0'.format(name)
        if type(value) != int:
            raise TypeError(type_err)
        if value <= 0:
            raise ValueError(val_err)
