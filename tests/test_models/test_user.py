#!/usr/bin/python3
"""Contains unittests for User class
"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """Tests User class
    """
    # create object instance of User Class
    instance_u = User()

    def test_class(self):
        """tests class instantiation and class attributes
        """
        # verificar si el objeto es una instancia User y de la clase principal
        self.assertIsInstance(instance_u, User)
        self.assertIsInstance(instance_u, BaseModel)

        # comprueba si los diccionarios contienen todos los atributos esperados
        # __dict__ solo contiene atributos establecidos, por lo que esto verifica si está establecido
        self.assertIn("id", instance_u.__dict__)
        self.assertIn("created_at", instance_u.__dict__)
        self.assertIn("updated_at", instance_u.__dict__)
        self.assertIn("email", User.__dict__)
        self.assertIn("password", User.__dict__)
        self.assertIn("first_name", User.__dict__)
        self.assertIn("last_name", User.__dict__)

        # verificar si los atributos de clase User se inicializaron correctamente
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertEqual(instance_u.email, "")
        self.assertEqual(instance_u.password, "")
        self.assertEqual(instance_u.first_name, "")
        self.assertEqual(instance_u.last_name, "")
