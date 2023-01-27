#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list
    Return number of elements printed
    """

    count = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i], end=""))
            count += 1
    except IndexError:
        x = len(my_list)

    return (count)
