#!/usr/bin/python3

"""class Square"""


class Square:
    """defines a square

    Class Square with Public methods (area, my_print) and getter and setter
    for attribute - size
    """

    def __init__(self, size=0):
        """Constructor

        Args:
            size (int, optional): size of the square. Defaults to 0
        """

        self.__size = size

    @property
    def size(self):
        """getter for size
        Returns integer - size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size
        Args:
            value (int): size of square
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Area method

        Returns: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """print method

        Prints to  stdout the square with the character #
        or an empty line if size is 0
        """

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
