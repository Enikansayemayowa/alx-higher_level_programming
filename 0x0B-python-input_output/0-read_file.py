#!/usr/bin/python3
"""Writing a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """Writing a function that reads a text file (UTF8)"""
    try:
        with open(my_file_0.txt, 'r', encoding="UTF8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"{my_file_0.txt} not fount")
    except Exception as e:
        print(f"An error occur as {e}")
