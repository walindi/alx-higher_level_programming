#!/usr/bin/python3

"""This module Defines a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix (list): A list of lists of ints/floats
        div (int/float): The divisor

    Raises:
        TypeError: if the matrix contains non-numbers
        TypeError: if rows of the matrix are not of same size
        TypeError: if div is not an int oor float
        ZeroDivisionError: if div is 0

    Returns:
        A new matrix which is the result of the division
    """

    if (type(matrix) is not list or
            not all(type(row) is list for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                "integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError ("division by zero")

    result = [[round(num / div, 2) for num in row] for row in matrix]

    return result
