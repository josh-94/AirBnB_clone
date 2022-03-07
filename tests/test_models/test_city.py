#!/usr/bin/python3
""" Contains unittests for City class
"""
import unittest
import os
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    """Tests City class
    """
    # create object instance of City Class
    instance_c = City()

    def test_class(self):
        """ tests class instantiation and class attributes
        """
        # comprueba si el objeto es una instancia de City y la clase principal
        self.assertIsInstance(instance_c, City)
        self.assertIsInstance(instance_c, BaseModel)

        # comprueba si los diccionarios contienen todos los atributos esperados
        # __dict__ solo contiene atributos establecidos, por lo que esto verifica si está establecido
        self.assertIn("id", instance_c.__dict__)
        self.assertIn("created_at", instance_c.__dict__)
        self.assertIn("updated_at", instance_c.__dict__)
        self.assertIn("name", City.__dict__)
        self.assertIn("state_id", City.__dict__)

        # verifica si el atributo de clase City se inicializó correctamente
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
        self.assertEqual(instance_c.name, "")
        self.assertEqual(instance_c.state_id, "")
