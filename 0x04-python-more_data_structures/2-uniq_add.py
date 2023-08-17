#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_num = set()
    for num in my_list:
        unique_num.add(num)
    result = sum(unique_num)
    return result
