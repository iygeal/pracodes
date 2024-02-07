#!/usr/bin/python3
"""The AirBnB Console"""
from datetime import datetime
from uuid import uuid4
from json import dump
from json import load


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
        else:
            # Create or assign ID, created_at and updated_at (new instances)
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

class FileStorage:
    """Class to be used to store files"""
    __filePath = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary named __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the key-value pair in __objects (class.id as key, obj as value)"""
        keyFormat = f"{obj.__class.__name__}.{obj.id}"
        FileStorage.__objects[keyFormat] = obj

    def save(self):
        # Declare an empty dict to hold the object we are serializing
        dictObj = {}
        # Loop and grab the objects (key-value pairs) we stored in __objects
        for key, val in FileStorage.__objects.items():
            # Convert the values to a dict using our save_to_dict() method
            dictObj[key] = val.save_to_dict()
            # Open the file path for writing (serialization)
            with open(FileStorage.__filePath, "w", encoding="utf-8") as jsonF:
                # Dump the serialized objects into the file
                dump(dictObj, jsonF)

    def reload(self):
        # Dict to hold all our defined classes (user_defined)
        definedClasses = {'MyBase': MyBase}
        # Attempt to open the json file in the filepath
        try:
            with open(FileStorage.__filePath, encoding="utf-8") as jsonStr:
                # Deserialize the json string in the file at the filepath
                deserialized = load(jsonStr)
                # Iterate over each obj's value in the deserialized dict
                for obj_values in deserialized.values():
                    # Get obj's class name from the '__class__' key
                    clsName = obj_values["__class__"]
                    # Get the actual class obj in the definedClasses dict
                    cls_obj = definedClasses[clsName]
                    # Create a new class instance with obj's values as argument
                    self.new(cls_obj(**obj_values))
        # Cathc FileNotFoundError and ignore if there's no file to deserialize
        except FileNotFoundError:
            pass






# Create a class instance and update it with a few attributes
my_model = MyBase()
my_model.name = "Lally Iygeal"
my_model.lally_age = 37
print(my_model.id)
print(my_model)
print(my_model.created_at)

print("\n------ serialized dictionary representation below ------\n")
my_model_json = my_model.save_to_dict()
print(my_model_json)
print("\n------ JSON of <'my_model'> below -----\n")
for key, value in my_model_json.items():
    print("\t{}: ({}) - {}".format(key, type(value), value))
print("\ -----deserialized to an instance below -----\n")

# Parse in the dictionary to the class constructor for deserialization
new_model = MyBase(**my_model_json)
print(new_model.id)
print(new_model)
print(new_model.created_at)
print("---------------- The two instances compared below ------\n")
print(new_model is my_model)