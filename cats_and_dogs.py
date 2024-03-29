#!/usr/bin/python3
"""Module that reads cats and dogs files"""


file_name = ['cats.txt, dogs.txt']

def read_stuff(file_name):
    """Function used to read stuff"""
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print(f"The file {file_name} doesn't extit")
    else:
        print(file_name)

read_stuff(file_name)