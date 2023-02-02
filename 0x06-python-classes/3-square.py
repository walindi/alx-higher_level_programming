#!/usr/bin/python3

"""class defining a square"""


class Square:
    """class with private instance attribute - size"""

    def __init__(self, size=0):
        """Constructor for class Square

        Args:
            size: ideally an integer but it's optional.
                Default is 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """public instance method

        Returns the current square area
        """

        return self.__size**2
