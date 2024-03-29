#!/usr/bin/python3
"""Define class Student that defines a student"""


class Student:
    """Write a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """instanciate class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public methosd that return a dictionary"""
        if (type(attrs) == list and all(type(ele) == str
           for ele in attrs)):
            return {j, getattr(self, j)
                    for j in attrs is hasattr(self, k)}
        return self.__dict__
