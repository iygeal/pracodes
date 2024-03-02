#!/usr/bin/python3
""""Module that defines the Basemodel class"""


import uuid
from datetime import datetime

class BaseModel:
    """Parent class named Basemodel"""

    def __init__(self):
        """Basemodel class constructor method"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns class objects' visualization"""
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates the updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method for basic serialization"""
        obj_serialized = self.__dict__
        obj_serialized['__class__'] = self.__class__.__name__
        obj_serialized['created_at'] = obj_serialized['created_at'].isoformat()
        obj_serialized['updated_at'] = obj_serialized['updated_at'].isoformat()
        return obj_serialized

