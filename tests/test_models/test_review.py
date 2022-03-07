#!/usr/bin/python3
""" Contains unittests for Review class
"""
import unittest
import os
from models.base_model import BaseModel
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """Tests Review class
    """
    # create object instance of Review Class
    instance_r = Review()

    def test_class(self):
        """tests class instantiation and class attributes
        """
        # verificar si el objeto es una instancia de Review y de la clase principal
        self.assertIsInstance(instance_r, Review)
        self.assertIsInstance(instance_r, BaseModel)

        # comprueba si los diccionarios contienen todos los atributos esperados
        # __dict__ solo contiene atributos establecidos, por lo que esto verifica si está establecido
        self.assertIn("id", instance_r.__dict__)
        self.assertIn("created_at", instance_r.__dict__)
        self.assertIn("updated_at", instance_r.__dict__)
        self.assertIn("place_id", Review.__dict__)
        self.assertIn("user_id", Review.__dict__)
        self.assertIn("text", Review.__dict__)

        # comprueba si el atributo de clase Review se inicializó correctamente
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertEqual(instance_r.place_id, "")
        self.assertEqual(instance_r.user_id, "")
        self.assertEqual(instance_r.text, "")
