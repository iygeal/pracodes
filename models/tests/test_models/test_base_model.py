#!/usr/bin/python3
"""Module to test the class BaseModel"""

from models_1.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseClass(unittest.TestCase):
    """The class used to test BaseModel"""

    def setUp(self):
        """Create instances for test methods"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_id_is_str(self):
        """Test if id is a string object"""
        self.assertIsInstance(self.b1.id, str)

    def test_id_is_unique(self):
        """Test if id attribute is unique"""
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_datetime_objects(self):
        """Test if created_at and updated_at are datetime objects"""
        created = self.b1.created_at
        updated = self.b1.updated_at
        self.assertIsInstance(created, datetime)
        self.assertIsInstance(updated, datetime)

    def test_save_method_updates_updated_at(self):
        """Test if save() updates updated_at"""
        self.assertNotEqual(self.b1.updated_at, self.b1.save())

    def test_str_method(self):
        """Test the __str__ method"""
        expected_str = f'[{type(self.b1).__name__}] ({self.b1.id}) {self.b1.__dict__}'
        self.assertEqual(expected_str, str(self.b1))