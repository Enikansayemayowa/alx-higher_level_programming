#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_value = []
    for k, a in a_dictionary.items():
        if a == value:
            new_value.append(k)

    for key in new_value:
        del a_dictionary[key]

    return a_dictionary
