#!/usr/bin/python3
"""Module to demonstrate writing to a file"""


filename = 'guest.txt'

guest_name = input("Please enter your name here: ")

with open(filename, 'w') as file_object:
    file_object.write(guest_name)