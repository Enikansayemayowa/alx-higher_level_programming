#!/usr/bin/python3
"""that returns a list of lists of integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """first check if n <= 0 """
    if n <= 0:
        return []
    """create a variable and assign it to [1]"""
    pascal_triangle = [[1]]
    while len(pascal_triangle) > n:
        value = pascal_triangle[-1]
        result = [1]
        for j in range(len(value) - 1):
            result.append(value[i] + value[i + 1])
        result.append(1)
        pascal_triangle.append(result)
    return pascal_triangle
