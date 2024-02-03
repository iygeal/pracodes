#!/usr/bin/python3
"""The AirBnB Console"""
from datetime import datetime
from uuid import uuid4


class MyBase:
    """The base class of the console"""
    def __init__(self, *args, **kwargs):
        # Discard the __class__ key if dict is not empty
        if kwargs:
            del kwargs["__class__"]
            for key, val in kwargs.items():
                # Grab date and time stamp keys and convert their values to datetime obj
                if key == "created_at" or key == "updated_at":
                    dtime_obj = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, dtime_obj)
                else:
                    setattr(self, key, val)
                    
        # Assign some common default attributes to all instances of this class
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save_update(self):
        """Update updated_at attribute with current date and time"""
        updated_at = datetime.now()

    def save_to_dict(self):
        """Serialization method that returns a dict object"""
        dictFormat = {}
        # Add a class key to identify the class name of the instance attribute
        dictFormat["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            # Get the values which are of datetime object type
            if isinstance(val, datetime):
                # Convert them to string objects in ISO format
                dictFormat[key] = val.isoformat()
            else:
                dictFormat[key] = val
        return dictFormat

    def __str__(self):
        """String representation for all class instances and their attributes"""
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

# Create a class instance and update it with a few attributes
my_model = MyBase()
my_model.name = "Lally Iygeal"
my_model.lally_age = 37
print(my_model)
my_model.save_update()
print("\n=== dictionary representation ===\n")
my_model_json = my_model.save_to_dict()
print(my_model_json)
print("\nJSON of my_model:\n")
for key, value in my_model_json.items():
    print("\t{}: ({}) - {}".format(key, type(value), value))