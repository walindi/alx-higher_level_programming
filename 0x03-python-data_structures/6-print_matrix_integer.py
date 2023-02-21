#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""

    for List in matrix:
        for num in List:
            if num != List[-1]:
                print("{}".format(num), end=" ")
            else:
                print("{}".format(num))
