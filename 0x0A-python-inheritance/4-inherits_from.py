#!/usr/bin/python3
"""if the object is an instance of a class that inherited."""


def inherits_from(obj, a_class):
    """Checks if an object is a class is inherited """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
