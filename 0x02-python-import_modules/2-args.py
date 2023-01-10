#!/usr/bin/python3

import sys

if __name__ == "__main__":
    n = len(sys.argv)

    """
    The list sys.argv contains the name of the script and all the arguments
    sys.argv[0] is the name of the script
    sys.argv[1] is the name of the first argument
    """
    if n == 1:
        print("0 arguments.")

    elif n == 2:
        str = sys.argv[n - 1]
        print("1 argument:")
        print("1: {}".format(str))

    elif n > 2:
        print("{} arguments:".format(n - 1))
        for i in range(1, n):
            str = sys.argv[i]
            print("{}: {}".format(i, str))
