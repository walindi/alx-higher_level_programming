#!/usr/bin/python3

"""class Square"""

class Square:
    """define a square"""

    def __init__(self, size=0):
        """initialize new square

        Args:
            size (int, optional): size of the square. Defaults to 0
        """

        self.__size = size

    @property
    def size(self):
        """retrieve/get the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square

        Args:
            value (int): size of square
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value


    def area(self):
        """Public instance method.
        Returns current square area
        """

        return self.__size**2
