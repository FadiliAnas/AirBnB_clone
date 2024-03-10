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
import json

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
    def save(self):
        json_dict = {}
        for k, v in FileStorage.__objects.items():
            json_dict[k] = v.to_dict()
        print("File path:", FileStorage.__file_path)
        with open(FileStorage.__file_path, 'w') as filejson:
            json.dump(json_dict, filejson, indent=4)

    def test_all(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], obj)

   


if __name__ == "__main__":
    unittest.main()
