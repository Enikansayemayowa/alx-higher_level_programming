#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # my_list is the initial list
    # search is the element to replace in the list
    # replace is the new element
    new_list = []
    for value in my_list:
        if value == search:
            new_list.append(replace)
        else:
            new_list.append(value)
    return new_list
