#!/usr/bin/python3

import sys

def print_addition_of_args():
    """Print the addition of all arguments."""
    total = sum(int(arg) for arg in sys.argv[1:])
    print(total)
    
if __name__ == "__main__":
    print_addition_of_args()
