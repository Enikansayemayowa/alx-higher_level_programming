#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_to_delete = []

    list_keys = list(a_dictionary.keys())

    for key in list_keys:
        if value == a_dictionary.get(key):
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
