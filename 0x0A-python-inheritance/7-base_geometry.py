#!/usr/bin/python3
"""base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """raise an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value is <= 0."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
