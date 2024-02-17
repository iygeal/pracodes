#!/usr/bin/python3
"""Module that defines a person and his choices"""


person_a = {
    'first_name': 'innocent',
    'last_name': 'anozie',
    'age': 34,
    'city': 'orlu',

}
person_b = {
    'first_name': 'iygeal',
    'last_name': 'williams',
    'age': 39,
    'city': 'vegas',
}
person_c = {
    'first_name': 'nelly',
    'last_name': 'joy',
    'age': 27,
    'city': 'nairobi',
}
people = [person_a, person_b, person_c]
for person in people:
    print(person)

