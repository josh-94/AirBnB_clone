#!/usr/bin/python3
"""This module contains the entry point
of the command interpreter
"""
import cmd
from models.engine import storage
from models.engine.utils import list_class
# from models.utils.utils import Utils


class HBNBCommand(cmd.Cmd):
    """Uses cmd methods to control command interpreter
    """
    # custom prompt:
    # intro = "Welcome to AirBnB command prompt"
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command exit the program
        """
        return True

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """Overwriting the emptyline method
        """
        return False

    def do_create(self, arg_instance):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        args = arg_instance.split()
        if self.not_class(arg_instance):
            return
        else:
            my_json = list_class[args[0]]()
            # my_json = list_class[arg_instance]()
            storage.save()
            print(my_json.id)

    def do_show(self, args_string):
        """Prints the string representation of an instance
        based on the class name and id
        """
        nm_arg = args_string.split()
        if self.not_class(args_string):
            return
        elif self.check_id(args_string):
            return
        else:
            my_jason = storage.all()
            for key, value in my_jason.items():
                c_name = value.__class__.__name__
                c_ide = value.id
                if c_name == nm_arg[0] and c_ide == nm_arg[1]:
                    print(value)

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id and saves the change into the JSON file
        """
        nm_arg = line.split()
        if self.not_class(line):
            return
        elif self.check_id(line):
            return
        else:
            key = '{}.{}'.format(nm_arg[0], nm_arg[1])
            __objects = storage.all()
            del __objects[key]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based on the class name or not.
            Ex: $ all BaseModel or $ all.
        """
        nm_arg = line.split()
        my_list = []
        all_ob = storage.all()
        if nm_arg[0] not in list_class:
            print("** class doesn't exist **")
        if nm_arg[0] is None:
            for key in all_ob.keys():
                value = all_ob.get(key)
                print_obj = '{}'.format(all_ob[key].__str__())
                print(print_obj)
                my_list.append(value)
        else:
            my_list = []
            all_ob = storage.all()
            for key, value in all_ob.items():
                obj_name = value.__class__.__name__
                if obj_name == nm_arg[0]:
                    my_list.append(value.__str__())
            print(my_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        nm_arg = line.split()
        if self.not_class(line):
            return
        elif self.check_id(line):
            return
        elif len(nm_arg) == 2:
            print("** attribute name missing **")
        elif len(nm_arg) == 3:
            print("** value missing **")
        else:
            value = nm_arg[3]
            key = '{}.{}'.format(nm_arg[0], nm_arg[1])
            __objects = storage.all()
            """La setattr()función establece el valor del
            atributo de un objeto.
            Note:
                toma tres parámetros:
                setattr(objeto, nombre, value)
                    objeto - objeto cuyo atributo debe establecerse
                    nombre - nombre del atributo
                    value - valor dado al atributo
            """
            setattr(__objects[key], nm_arg[2], value)
            storage.save()

    @staticmethod
    def not_class(clss_name):
        """Checks if given valid class name argument
        Prints error message if missing or invalid
        """
        num_arg = clss_name.split()
        if len(clss_name) == 0:
            print("** class name missing **")
            return True
        elif num_arg[0] not in list_class:
            print("** class doesn't exist **")
            return True
        return False

    @staticmethod
    def check_id(clss_id):
        """Checks if given valid instance id argument
        Prints error message if missing or invalid
        """
        num_arg = clss_id.split()
        if len(num_arg) == 1:
            print("** instance id missing **")
            return True
        elif (num_arg[0] + "." + num_arg[1]) not in list(storage.all().keys()):
            print("** no instance found **")
            return True
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
