#!/usr/bin/python3
"""Module that contains a script to add numbers"""


print("We are going to do some additions")
print("Enter 'quit' at any point to exit the calculator")
while True:
    try:
        first_number = input("Please enter first number: ")
        if first_number.lower() == 'quit':
            print("Calculator closed")
            break
        first_number = int(first_number)

        second_number = input("Now enter second number: ")
        if second_number.lower() == 'quit':
            print("Calculator closed")
            break
        second_number = int(second_number)
        result = (first_number) + (second_number)

        print(f"The sum of first number and second number is {result}")

    except ValueError:
        print("Please enter only numbers")