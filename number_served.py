#!/usr/bin/python3
"""Module that defines a class named Restaurant"""


class Restaurant:
    """The Restaurant class"""
    def __init__(self, restaurant_name, cuisne_type):
        """Class constructor method"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisne_type
        self.number_served = 0

    def describe_restaurant(self):
        """Method that describes a restuarant"""
        print(f"The name of the restaunt is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        """Indicates open restaurant"""
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, served):
        """Sets value to number served"""
        self.number_served = served

    def increment_number_served(self, served1):
        """Method that increments number served"""
        self.number_served += served1

restaurant = Restaurant('Iygeal Eateries', 'Pan African')
restaurant.number_served = 50
print(f"The number of guests served is {restaurant.number_served}")
restaurant.number_served = 55
print(f"The number of guests served increased to {restaurant.number_served}")
restaurant.set_number_served(57)
print(f"The number of guests served increased to {restaurant.number_served}")
restaurant.increment_number_served(13)
print(f"The number of guests served increased to {restaurant.number_served}")
