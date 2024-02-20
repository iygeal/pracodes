#!/usr/bin/python3
"""Module to use for unittest tests"""


def city_functions(city, country, population=0):
    """Function that accepts city, country arguments"""
    if population:
        location = f"{city}, {country} - population {population}"
    else:
        location = f"{city}, {country}"
    return location.title()