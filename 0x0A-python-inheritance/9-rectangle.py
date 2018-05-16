#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
	def __init__(self, width, height):
		self.integer_validator('width', width)
		self.integer_validator('height', height)
		self.__width = width
		self.__height = height

	def area(self):
		return self.__width * self.__height

	def __str__(self):
		w = self.__width
		h = self.__height
		cls = self.__class__.__name__
		msg = "[{}] {}/{}".format(cls, w, h)
		return msg
