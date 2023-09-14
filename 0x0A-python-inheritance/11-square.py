#!/usr/bin/python3
"""A Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square."""

    def __init__(self, size):
        """initialization of a Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
