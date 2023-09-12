#!/usr/bin/python3
""" function that writes a string to a text file
(UTF8) and returns the number of"""


def append_write(filename="", text=""):
    """ function that writes a string to a text file
    (UTF8) and returns the number of"""
    with open(filename, "a", encoding="utf-8") as file:
        char_written = file.write(text)
