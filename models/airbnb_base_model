#!/usr/bin/python3

"""Module that defines a class named BaseModel"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class definition
    """

    def __init__(self, *args, **kwargs):
        """Constructor method to initialize a new BaseModel instance"""
        if kwargs:
            # Exclude '__class__' from deserialization
            del kwargs["__class__"]
            for key, value in kwargs.items():
                # Convert 'created_at' and 'updated_at' to datetime objects
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            # New instances: Generate ID and timestamps
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def save(self):
        """Updates the updated_at attribute with the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method for serialization"""
        serialized = dict(self.__dict__)
        serialized['__class__'] = self.__class__.__name__
        serialized.update({"created_at": self.created_at.isoformat(
        ), "updated_at": self.updated_at.isoformat()})
        return serialized

    def __str__(self):
        """Returns a visualization of the class objects"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

