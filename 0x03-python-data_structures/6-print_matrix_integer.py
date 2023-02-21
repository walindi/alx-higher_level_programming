#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""

    if matrix == [[]]:
        print()

    for List in matrix:
        for num in List:
            if num != List[-1]:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num))
