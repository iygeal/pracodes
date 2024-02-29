#!/usr/bin/python3
"""Module that provides a function to count words"""


def count_words(filename):
    """The function that counts words"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print(f"The file {filename} does not exist")
        pass
    else:
        words = contents.split()
        count = len(words)
        print(f"The file {filename} has approximately {count} words.")

filenames = ['alice.txt', 'guest', 'little_women.txt', 'iygeal.txt']
for filename in filenames:
    count_words(filename)