#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”:"""


def save_to_json_file(my_obj, filename):
    """Write a function that creates an Object from a “JSON file”:"""
    with open(fileename, "w") as file:
        json.dump(my_obj, file)
