#!/usr/bin/python3
"""A module that defines dictionaries of dictionaries"""


cities = {
    'orlu': {'country': 'nigeria', 'population': '5 million', 'fact': 'has bautiful women'},
    'owerri': {'country': 'naija', 'population': '60 millon', 'fact': 'is small'},
    'nyc': {'country': 'USA', 'population': 1000, 'fact': 'has gun fights'}
}
for city, info in cities.items():
    print(f'\nName of city is {city.upper()}')
    print("\tThe city is in " + info['country'])
    print(f'\tPopulation of city is {info["population"]}')
    print(f'\tFun fact about this city is that it {info["fact"]}')