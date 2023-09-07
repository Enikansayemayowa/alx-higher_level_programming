#!/usr/bin/python3
"""Defines a Rectangle class."""
class Rectangle:
    """Defines a Rectangle class."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """declaring the getter for width"""
    @property
    def width(self):
        return self.__width

"""width setter"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """declaring the getter for height"""
    @property
    def height(self):
        return self.__height

    """setter for height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
