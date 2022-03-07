#!/usr/bin/python3
""" Module of Unittests
"""
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for the class BaseModel
    """
    instance_bm = BaseModel()

    def test_init(self):
        """Test for the method __init__
        """
        # comprobar si el objeto es una instancia de BaseModel
        self.assertIsInstance(instance_bm, BaseModel)
        # comprobar si el diccionario contiene todos los atributos esperados
        self.assertIn("id", instance_bm.__dict__)
        self.assertIn("created_at", instance_bm.__dict__)
        self.assertIn("updated_at", instance_bm.__dict__)

        # comprobar si los atributos de la instancia pública tienen
        # el tipo de dato correcto.
        self.assertIsInstance(my_instance.id, str)
        self.assertIsInstance(my_instance.created_at, datetime)
        self.assertIsInstance(my_instance.updated_at, datetime)

    def test_str(self):
        """ Tests for the method __str__
        """
        clas = type(instance_bm).__name__
        ide = instance_bm.id
        dictt = instance_bm.__dict__
        my_str = "[{}] ({}) {}".format(clas, ide, dictt)

        # comprobar si __str__ devuelve la representación de cadena esperada
        self.assertEqual(instance_bm.__str__(), my_str)

    def test_save(self):
        """Test for the method save
        """
        # comprueba que update_at cambia manteniendo los
        # valores antes y después de guardar.
        a = instance_bm.updated_at
        instance_bm.save()
        b = instance_bm.updated_at
        self.assertNotEqual(a, b)

    def test_to_dict(self):
        """ Tests to_dict method
        """
        repr_dict = instance_bm.to_dict()
        # compruebe si todas las claves de obj.__dict__ y __class__ en dict_rep
        for key in instance_bm.__dict__:
            self.assertIn("{}".format(key), repr_dict)
        self.assertIn("__class__", repr_dict)

        # comprobar si los valores del diccionario son del tipo correcto
        self.assertIsInstance(repr_dict["id"], str)
        self.assertIsInstance(repr_dict["created_at"], str)
        self.assertIsInstance(repr_dict["updated_at"], str)
        self.assertIsInstance(repr_dict["__class__"], str)

        # comprobar si los valores del diccionario son correctos
        self.assertEqual(repr_dict["id"], obj.id)
        self.assertEqual(repr_dict["__class__"], type(obj).__name__)
        string = str(datetime.isoformat(instance_bm.created_at))
        self.assertEqual(repr_dict["created_at"], string)
        string = str(datetime.isoformat(instance_bm.updated_at))
        self.assertEqual(repr_dict["updated_at"], string)
