#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """instance attributes, each with its own public"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width of the Rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def height(self):
        """get the height of the Rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x of the Rectangle."""

        return self.__x

    @x.setter
    def x(self, value):
        """Set the of the Rectangle."""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """get the y of the Rectangle."""

        return self.__y

    @y.setter
    def y(self, value):
        """Set the y of the Rectangle."""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
