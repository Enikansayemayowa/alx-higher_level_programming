#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_value = list(a_dictionary.keys())
    for k in new_value:
        if value == a_dictionary.get(k):
            del a_dictionary[k]

    return a_dictionary
