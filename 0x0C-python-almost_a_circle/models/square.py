#!/usr/bin/python3
"""documentation"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """documentation"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """doc"""
        rep = '[Square] ({}) {}/{} - {}'
        return rep.format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """doc"""
        attrs = ['id', 'size', 'x', 'y']
        return self.make_dict(self, attrs)

    @staticmethod
    def attrs():
        """doc"""
        return ['id', 'size', 'x', 'y']

    def update(self, *args, **kwargs):
        """doc"""
        attrs = ['id', 'size', 'x', 'y']
        self.setattrs_from_splat(self, attrs, *args, **kwargs)

    @property
    def size(self):
        """doc"""
        return self.width

    @size.setter
    def size(self, value):
        """doc"""
        self.width = value
        self.height = value
