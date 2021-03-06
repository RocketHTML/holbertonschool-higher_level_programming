#!/usr/bin/python3
"""documentation"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """documentation"""
    def __init__(self, size, x=0, y=0, id=None):
        """documentation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """documentation"""
        rep = '[Square] ({}) {}/{} - {}'
        return rep.format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """documentation"""
        attrs = ['id', 'size', 'x', 'y']
        return self.make_dict(self, attrs)

    @staticmethod
    def attrs():
        """documentation"""
        return ['id', 'size', 'x', 'y']

    def update(self, *args, **kwargs):
        """documentation"""
        attrs = ['id', 'size', 'x', 'y']
        self.setattrs_from_splat(self, attrs, *args, **kwargs)

    @property
    def size(self):
        """documentation"""
        return self.width

    @size.setter
    def size(self, value):
        """documentation"""
        self.width = value
        self.height = value
