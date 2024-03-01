#!/usr/bin/python3
"""Module that defines the Base class"""


class Base:
    """The parent class named Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of the Base class"""
        if id is not None:
            self.id = id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects