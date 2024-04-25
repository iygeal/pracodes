#!/usr/bin/python3
"""Test file for sqlalchemy"""

from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql://iygeal_alx:Alxstudent77!@localhost/sample", echo=True)


with engine.connect() as connection:
    result = connection.execute(text('SELECT "Hello"'))
    print(result.all())
