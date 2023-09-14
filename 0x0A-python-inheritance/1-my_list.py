#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """that prints the list, but sorted (ascending sort)"""

    def print_sorted(self):
        """Print a list in sorte."""
        print(sorted(self))
