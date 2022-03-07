#!/usr/bin/python3
""" Contains unittests for Amenity class
"""
import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """ Tests Amenity class
    """
    # create object instance of Amenity Class
    instance_a = Amenity()

    def test_class(self):
        """ tests class instantiation and class attributes
        """
        # comprueba si el objeto es una instancia de Amenity
        # y de la clase principal
        self.assertIsInstance(instance_a, Amenity)
        self.assertIsInstance(instance_a, BaseModel)

        # comprobar si los diccionarios contienen todos los atributos esperados
        # __dict__ solo contiene atributos establecidos, por lo que esto verifica si está establecido
        self.assertIn("id", instance_a.__dict__)
        self.assertIn("created_at", instance_a.__dict__)
        self.assertIn("updated_at", instance_a.__dict__)
        self.assertIn("name", Amenity.__dict__)

        # verificar si el atributo de clase de Amenity se inicializó correctamente
        self.assertEqual(Amenity.name, "")
        self.assertEqual(instance_a.name, "")
