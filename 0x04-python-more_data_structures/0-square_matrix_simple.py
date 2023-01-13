#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newMatrix = [[num**2 for num in row] for row in matrix]
    return newMatrix
