#!/usr/bin/python3

"""Defines a Base model class"""


class Base:
    """Base of all other classes in the project

    Attributes:
        __nb_objects (int): The number of instantiated bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of the new base

        Args:
            id (int): id of new base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
