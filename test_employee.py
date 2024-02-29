#!/usr/bin/python3
"""Module to test Employee class"""
from employee import Employee
import unittest


class TestEmployee(unittest.TestCase):
    """The test class to test Employee"""

    def setUp(self):
        """Create necessary items for test methods"""
        self.my_employee = Employee('Iygeal', 'Anozie', 300000)

    def test_give_default_raise(self):
        """Tests for default raise"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 305000)

    def test_give_custom_raise(self):
        """Tests give_raise() with custom raise"""
        self.my_employee.give_raise(30000)
        self.assertEqual(self.my_employee.salary, 330000)

if __name__ == '__main__':
    unittest.main()