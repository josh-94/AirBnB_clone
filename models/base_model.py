  #!/usr/bin/python3
"""Class BaseModel that defines all common attributes/methods for other classes
"""

from datetime import datetime
from models import storage
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        """initializes all attributes 
		Note: 
		    If a dictionary is provided, dictionary values are used
        """
        if len(kwargs) != 0:'''if kwargs is not empty'''
        '''Loop through the key and value in the entered elements'''
        for key, value in kwargs.items():
            '''Assign the key to the current date of creation and update'''
            if key == "created_at" or key == "updated_at":
                my_time = datetime.strptime(value, "%Y-%m-%dT-%H:%M:%S.%f")
                setattr(self, key, my_time)
            elif key != "__class__":
                setattr(self, key, value)
        else:
            '''assign random id'''
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            '''If it is a new instance we call the method new(self)'''
            storage.new(self)

def __str__(self):
    """returns class name, id and attribute dictionary
    """
    c_name = self.__class__.__name__
    print("[{}] ({}) {}".format(c_name, self.id, self.__dict__))

def save(self):
    """updates last update time
    """
    self.updated_at = datetime.now()
    storage.save(self)

def to_dict(self):
    """ returns a dictionary representation of instance
    Note:
        times are stored in ISO format
    """
    my_dict = self.__dict__
    my_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
    my_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
    my_dict["__class__"] = self.__class__.__name__
    return my_dict