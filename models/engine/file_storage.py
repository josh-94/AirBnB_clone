#!/usr/bin/python3
"""
Defines the FileStorage class
"""
import json
from models.base_model import BaseModel
from models.engine.utils import list_class


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances
    Attributes:
        __file_path (str): path to JSON file
        __objects (dict): will store objects by class.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary of all saved objects
        """
        return self.__objects

    def new(self, obj):
        """stores obj in __objects dictionary:
                key = "<obj class name>.id"
                value = obj.to_dict()
        """
        key = obj.__class__.__name__ + "." + obj.id
        value = obj
        self.__objects[key] = value

    def save(self):
        """serializes __object to the JSON file
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as my_file:
            my_file.write(json.dumps(my_dict))

    def reload(self):
        """deserializes JSON file to __objects
        Note:
            if JSON file (__file_path) does not exist, nothing is done.
        """
        try:
            with open(self.__file_path, 'r') as j_file:
                # deserializacion del archivo
                dic_obj = json.load(j_file)
            # recorre el contenido del archivo deserializado
            for key, value in dic_obj.items():
                # obtener el diccionario
                cl_name = value["__class__"]
                self.new(list_class[cl_name](**value))
        except Exception:
            pass
