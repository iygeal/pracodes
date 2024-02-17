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

user1 = User('Iygeal', 'Anozie', 34)
user1.greet_user()
user1.describe_user()
user1.increment_login_attempts()
print(f"We have {user1.login_attempts} login attempts")
user1.increment_login_attempts()
print(f"We have {user1.login_attempts} login attempts")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"We have {user1.login_attempts} login attempts")
user1.reset_login_attenpts()
print(f"We have {user1.login_attempts} login attempts")