#!/usr/bin/python3
"""Module that defines a user"""


class User:
    """The User class"""

    def __init__(self, first_name, last_name, age):
        """Constructor of the class User"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Method that prints a summary of the user"""
        print(f"User summary: {self.first_name}, {self.last_name}, {self.age}")

    def greet_user(self):
        """Prints personal greeting"""
        print(f"Hello {self.first_name}, how is the family?")

    def increment_login_attempts(self):
        """Increments login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attenpts(self):
        """Resets login_attempts to 0"""
        self.login_attempts = 0

class Admin(User):
    """Admin class that inherits from User"""
    def __init__(self, first_name, last_name, age):
        """Initializes attributes of the User class"""
        super().__init__(first_name, last_name, age)
        self.privileges = ['can add posts', 'can delete posts', 'cab ban user']

    def show_privileges(self):
        """Displays admin privileges"""
        print("The admin: " + str(self.privileges))

iygeal = Admin('Iygeal', 'Anozie', 34)
iygeal.describe_user()
iygeal.show_privileges()