#!/usr/bin/python3
"""
Test for filestorage
"""
import unittest
import os
from models.base_model import BaseModel
from models.storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        key1 = "{}.{}".format(obj1.__class__.__name__, obj1.id)
        key2 = "{}.{}".format(obj2.__class__.__name__, obj2.id)

        self.assertIn(key1, new_storage.all())
        self.assertIn(key2, new_storage.all())

    def test_reload_file_not_found(self):
        # Make sure reload does not raise FileNotFoundError
        self.assertIsNone(self.storage.reload())


if __name__ == '__main__':
    unittest.main()

