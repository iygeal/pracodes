#!/usr/bin/python3
""""Module that records guest book"""
from rich.console import Console


console = Console()

filename = 'guest_book.txt'

while(True):
    console.print("[italic]Type 'quit' to exit at any time[/italic]")

    username = input("What is your name? ")
    if username == 'quit':
        print('Guest book closed')
        break

    print(f"Thanks for dopping by, {username}!")

    with open(filename, 'a') as file_object:
        file_object.write(username + '\n')