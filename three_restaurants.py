#!/usr/bin/python3
"""Module that defines a class named Restaurant"""


class Restaurant:
    """The Restaurant class"""
    def __init__(self, restaurant_name, cuisne_type):
        """Class constructor method"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisne_type

    def describe_restaurant(self):
        """Method that describes a restuarant"""
        print(f"The name of the restaunt is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        """Indicates open restaurant"""
        print(f"{self.restaurant_name} is now open.")

restaurant_0 = Restaurant("Iygeal Eateries", "Pan African")
restaurant_1 = Restaurant("Mama Put", "Sushi")
restaurant_2 = Restaurant("Index Food", "Consti-free")
restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()