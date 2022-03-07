#!/usr/bin/python3
""" Contains unittests for Place class
"""
import unittest
import os
from models.base_model import BaseModel
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """Tests Place class
    """
    # create object instance of Place Class
    instance_p = Place()

    def test_class(self):
        """tests class instantiation and class attributes
        """
        # verifica si el objeto es una instancia de Place y clase principal
        self.assertIsInstance(instance_p, Place)
        self.assertIsInstance(instance_p, BaseModel)

        # comprobar si los diccionarios contienen todos los atributos esperados
        # __dict__ solo contiene atributos establecidos, por lo que esto verifica si está establecido
        self.assertIn("id", instance_p.__dict__)
        self.assertIn("created_at", instance_p.__dict__)
        self.assertIn("updated_at", instance_p.__dict__)
        self.assertIn("city_id", Place.__dict__)
        self.assertIn("user_id", Place.__dict__)
        self.assertIn("name", Place.__dict__)
        self.assertIn("description", Place.__dict__)
        self.assertIn("number_rooms", Place.__dict__)
        self.assertIn("number_bathrooms", Place.__dict__)
        self.assertIn("max_guest", Place.__dict__)
        self.assertIn("price_by_night", Place.__dict__)
        self.assertIn("latitude", Place.__dict__)
        self.assertIn("longitude", Place.__dict__)
        self.assertIn("amenity_ids", Place.__dict__)

        # verificar si el atributo de clase Place se inicializó correctamente
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
        self.assertEqual(instance_p.city_id, "")
        self.assertEqual(instance_p.user_id, "")
        self.assertEqual(instance_p.name, "")
        self.assertEqual(instance_p.description, "")
        self.assertEqual(instance_p.number_rooms, 0)
        self.assertEqual(instance_p.number_bathrooms, 0)
        self.assertEqual(instance_p.max_guest, 0)
        self.assertEqual(instance_p.price_by_night, 0)
        self.assertEqual(instance_p.latitude, 0.0)
        self.assertEqual(instance_p.longitude, 0.0)
        self.assertEqual(instance_p.amenity_ids, [])
