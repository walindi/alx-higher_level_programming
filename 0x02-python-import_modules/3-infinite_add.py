#!/usr/bin/python3

import sys

if __name__ == "__main__":
    """Print sum of all arguments"""

    length = len(sys.argv)
    """
    sys.argv list includes the name of the script as the first item
    all items in the list are of str type
    """
    sum = 0
    index = (length - 1)

    for i in range(index):
        """
        start from second int
        """
        sum += int(sys.argv[i + 1])
    print(sum)
