#!/usr/bin/python3
"""Module that reads from a file"""


file_name = 'read_files.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

file_string = ""
for line in lines:
    file_string += line.strip()
print(file_string)
print(len(file_string))