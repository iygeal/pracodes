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


class IceCreamStand(Restaurant):
    """A class that inherits from Restaurant class"""
    def __init__(self, restaurant_name, cuisine_type):
        """This method initializes attributes of the base class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['vanilla', 'chocolate', 'strawberry']

    def display_flavours(self):
        print(f"Our icecream flavours are: {self.flavours}")

my_ice_cream_stand = IceCreamStand('Icy_Iygeal', 'East_Coast Yummies')
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavours()
