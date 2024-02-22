#!/usr/bin/python3
"""Module to test Employee class"""
from employee import Employee
import unittest


class TestEmployee(unittest.TestCase):
    """The test class to test Employee"""

    def setUp(self):
        """Create necessary items for test methods"""
        my_employee = Employee('Iygeal', 'Anozie', '$300,000')

    def test_give_default_raise(self):
        """Tests for default raise"""
        default = my_employee.give_raise()
        self.assertEqual