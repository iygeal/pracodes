#!/usr/bin/python3
"""Module that defines a class called Employee"""


class Employee:
    """The Employee class"""

    def __init__(self, first, last, salary):
        """Constructor method"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, raise_salaray=5000):
        """Method to control salary raise"""
        self.salary += raise_salaray

