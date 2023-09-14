#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """instance of class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        """ method of class"""
        def to_json(self, attrs=None):
            """that retrieves a dictionary representation of a Student"""
            if (type(attrs) == list and all(type(element) == str
               for element in attr)):
                return {j: getattr(self, j)
                        for j in attrs if hasattr(self, j)}

        def to_json(self, attrs=None):
            """replaces all attributes of the Student instance:"""
            for j, i in json.items():
                setattr(self, j, i)
