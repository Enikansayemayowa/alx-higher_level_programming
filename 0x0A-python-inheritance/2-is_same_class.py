#!/usr/bin/python3
"""Defines a class checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly same"""
    if type(obj) == a_class:
        return True
    return False
