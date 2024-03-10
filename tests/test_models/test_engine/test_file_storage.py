#!/usr/bin/python3
"""
Test of file Storage
"""
import unittest
from unittest.mock import patch
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], obj)

    def test_save_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

        storage_reloaded = FileStorage()
        storage_reloaded._FileStorage__file_path = self.file_path
        storage_reloaded.reload()

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage_reloaded.all())
        self.assertEqual(storage_reloaded.all()[key].to_dict(), obj.to_dict())


if __name__ == "__main__":
    unittest.main()
