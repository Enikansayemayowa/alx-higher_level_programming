#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”:"""


def load_from_json(my_obj, filename):
    """Write a function that creates an Object from a “JSON file”:"""
    with open(fileename) as file:
        json.load(file)
