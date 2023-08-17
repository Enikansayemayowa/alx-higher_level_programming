#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_value = []
    for a in a_dictionary:
        if a == a_dictionary[a]:
            del a_dictionary[a]
        else:
            return a_dictionary
