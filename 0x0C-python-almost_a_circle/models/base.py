#!/usr/bin/python3


"""This is the "base" for all other classes"""


class Base:
    """This is the "base" for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):

        """Initialize a new Base."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
