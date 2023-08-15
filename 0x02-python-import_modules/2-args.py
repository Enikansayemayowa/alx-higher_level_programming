#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_arg = len(sys.argv) - 1
    if num_arg == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(num_arg, "s" if num_arg != 1 else ""))
        for j in range(num_arg):
            print("{}: {}".format(j + 1, sys.argv[j + 1]))
