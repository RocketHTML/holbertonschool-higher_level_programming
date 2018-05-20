#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @classmethod
    def save_to_file(cls, list_objs):
        with open('Rectangle.json', mode='w', encoding='utf-8') as f:
            json.dump(f, list_objs)

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @staticmethod
    def make_dict(obj, attrs):
        ret = {}
        for key in attrs:
            ret[key] = getattr(obj, key)
        return ret

    @staticmethod
    def setattrs_from_splat(obj, attrs, *args, **kwargs):
        for i in range(len(args)):
            setattr(obj, attrs[i], args[i])
        if len(args) == 0:
            for a in attrs:
                if a in kwargs:
                    setattr(obj, a, kwargs[a])
