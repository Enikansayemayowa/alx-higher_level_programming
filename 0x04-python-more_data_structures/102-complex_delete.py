#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_value = []
    for k, a in a_dictionary.items():
        if a == value:
            del a_dictionary[k]
    return a_dictionary
