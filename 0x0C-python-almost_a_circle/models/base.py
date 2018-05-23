#!/usr/bin/python3
"""documentation"""
import json
import inspect
import csv
import turtle


class Base:
    """documentation"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def draw(list_rectangles, list_squares):
        def drawrect(turt, x, y, width, height):
            turt.setpos(x, y)
            turt.down()
            turt.goto(x+width, y)
            turt.goto(x+width, y+height)
            turt.goto(x, y+height)
            turt.goto(x, y)
            turt.up()
        turgle = turtle.Turtle()
        for r in list_rectangles:
            turgle.color('red')
            drawrect(turgle, r.x, r.y, r.width, r.height)
        for s in list_squares:
            turgle.color('blue')
            drawrect(turtle, s.x, s.y, s.width, s.height)

    @classmethod
    def load_from_file_csv(cls):
        name = cls.__name__
        ret = []
        try:
            with open("{}.csv".format(name), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for data in reader:
                    entry = {}
                    for k, v in zip(cls.attrs(), data):
                        entry[k] = int(v)
                    ret.append(cls.create(**entry))
                return ret
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file(cls):
        name = cls.__name__
        try:
            with open("{}.json".format(name), 'r', encoding='utf-8') as f:
                l = json.load(f)
                return [cls.create(**d) for d in l]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        args = inspect.getargspec(cls).args
        notouch = ['self']
        if dictionary['id'] is None:
            notouch.append('id')
        attrs = {}
        for att in args:
            if att in dictionary and att not in notouch:
                attrs[att] = 98
        obj = cls(**attrs)
        obj.update(**dictionary)
        return obj

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        name = cls.__name__
        attrs = cls.attrs()
        csv_objs = []
        for obj in list_objs:
            obj_attrs = []
            for att in attrs:
                obj_attrs.append(getattr(obj, att))
            csv_objs.append(obj_attrs)
        with open('{}.csv'.format(name), mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            for row in csv_objs:
                writer.writerow(row)

    @classmethod
    def save_to_file(cls, list_objs):
        """documentation"""
        name = cls.__name__
        with open('{}.json'.format(name), mode='w', encoding='utf-8') as f:
            if list_objs is None:
                json.dump([], f)
            else:
                json.dump(list_objs, f)

    @staticmethod
    def to_json_string(list_dictionaries):
        l = list_dictionaries
        if l is None or len(l) == 0:
            return "[]"
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
            if args[i] is not None:
                setattr(obj, attrs[i], args[i])
        if len(args) == 0:
            for a in attrs:
                if a in kwargs and kwargs[a] is not None:
                    setattr(obj, a, kwargs[a])
