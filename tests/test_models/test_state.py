#!/usr/bin/python3
"""Contains unittests for State class
"""
import unittest
import os
from models.base_model import BaseModel
from models.state import State


class TestStateClass(unittest.TestCase):
    """Tests State class
    """
    # create object instance of State Class
    instance_s = State()

    def test_class(self):
        """tests class instantiation and class attributes
        """
        # comprueba si el objeto es una instancia State y de la clase principal
        self.assertIsInstance(instance_s, State)
        self.assertIsInstance(instance_s, BaseModel)

        # comprueba si los diccionarios contienen todos los atributos esperados
        # __dict__ solo contiene atributos establecidos,
        # por lo que esto verifica si está establecido
        self.assertIn("id", instance_s.__dict__)
        self.assertIn("created_at", instance_s.__dict__)
        self.assertIn("updated_at", instance_s.__dict__)
        self.assertIn("name", State.__dict__)

        # verificar si el atributo de clase State se inicializó correctamente
        self.assertEqual(State.name, "")
        self.assertEqual(instance_s.name, "")
