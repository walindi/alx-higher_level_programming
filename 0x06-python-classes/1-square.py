#!/usr/bin/python3

"""class Square"""


class Square:
    """"Class with private attribute size"""

    def __init__(self, size):
        """Constructor

        Args:
            size: private attribute for size of the new square
        """
        self.__size = size
