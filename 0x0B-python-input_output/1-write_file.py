#!/usr/bin/python3
""" function that writes a string to a text file
(UTF8) and returns the number of"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file
    (UTF8) and returns the number of"""
    with open(filename, "w", encoding="utf-8") as file:
        char_written = f.write(text)
    return char_written
