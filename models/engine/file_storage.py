#!/usr/bin/python3
"""Class that serializes instances to a JSON file
and deserializes JSON file to instances
"""

class FileStorage:
	""" serializes to / deserializes from a JSON file
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
		key =  obj.__class__.__name__ + "." + obj.id
		value = obj.to_dict()

		__objects[key] = value

	def save(self):
		"""serializes __object to the JSON file
		"""
		my_dict = {}
		for key, value in ...nothing

	def reload(self):
		"""deserializes JSON file to __objects
        Note:
            if JSON file (__file_path) does not exist, nothing is done.
        """    
		