#!/usr/bin/python3
"""class MyInt that inherits from int."""


class MyInt(int):
    """int operators == and !=."""

    def __equal__(self, value):
        """Override == opeartor with != behavior."""
        return self.area != value

    def __notEqual__(self, value):
        """Override != operator with == behavior."""
        return self.arear == value
