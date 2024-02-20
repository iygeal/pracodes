#!/usr/bin/python3
"""Test module to test city_functions"""

from city_functions import city_functions
import unittest


class City_Test_Case(unittest.TestCase):
    """Class to test the city_functions"""
    def test_city_country(self):
        """Method to test for city and country inputs"""
        city_results = city_functions('lagos', 'nigeria')
        self.assertEqual(city_results, 'Lagos, Nigeria')

    def test_city_country_population(self):
        """Tests inputs containing city, country and population"""
        city_results = city_functions('Orlu', 'Nigeria', 5000000)
        self.assertEqual(city_results, 'Orlu, Nigeria - Population 5000000')

unittest.main()