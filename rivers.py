#!/usr/bin/python3
"""Module that prints rivers and countries"""


rivers = {
    'nile': 'egypt',
    'niger': 'nigeria',
    'benue': 'ivory coast',

}
countries = ['egypt', 'nigeria', 'china', 'ivory coast', 'malawai', 'ghana']
for c in countries:
    if c not in rivers.values():
        print(f"Okay fellows, {c.title()} has no river!")

