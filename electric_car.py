#!/usr/bin/python3
"""Module that defines car classes"""


class Car:
    """The base Car class"""
    def __init__(self, make, model, year):
        """The constructor method"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Decriptive name of the car"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Reads the odometer"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Updates the odometer reading"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increments the odometer reading"""
        self.odometer_reading += miles

class Battery:
    """Class dedicated to battery"""
    def __init__(self, battery_size=70):
        """Constructor method for the battery"""
        self.battey_size = battery_size

    def describe_battery(self):
        """Decribes the battery"""
        print("This car has a " + str(self.battey_size) + "-kWh battery.")

    def get_range(self):
        """Indicates the range offered by the battery"""
        if self.battey_size == 70:
            range = 240
        elif self.battey_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrades the battery capacity"""

class ElectricCar(Car):
    """Electric car class that inherits from Car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()





