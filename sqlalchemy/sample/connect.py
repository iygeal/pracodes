#!/usr/bin/python3
"""Test file for sqlalchemy"""

from sqlalchemy import create_engine, text

engine = create_engine("mysql:///sample.db")


with engine.connect() as connection:
    result = connection.execute(text('SELECT "Hello"'))
    print(result.all())