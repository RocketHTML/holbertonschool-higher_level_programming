#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return vars(self)
        else:
            d = {}
            for k, v in vars(self):
                if k in attrs:
                    d[k] = v
            return d
