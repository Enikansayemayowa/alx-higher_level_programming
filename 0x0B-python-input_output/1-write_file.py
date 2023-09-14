#!/usr/bin/python3
""" function that writes a string to a text file
(UTF8) and returns the number of"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file
    (UTF8) and returns the number of"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
        """char_written = file.write(text)
    return char_written"""
