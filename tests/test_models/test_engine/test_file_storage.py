#!/usr/bin/python3
""" Test of file Storage """
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage"""

    def setUp(self):
        """Set up the test cases"""
        self.storage = FileStorage()
        setattr(FileStorage, "_FileStorage__objects", {})
    
    def tearDown(self):
        """Clean up"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all_method_exists(self):
        """Test if the 'all' method exists"""
        self.assertTrue(hasattr(models.storage, "all"))

    def test_new_method_exists(self):
        """Test if the 'new' method exists"""
        self.assertTrue(hasattr(models.storage, "new"))

    def test_reload_method_exists(self):
        """Test if the 'reload' method exists"""
        self.assertTrue(hasattr(models.storage, "reload"))

    def test_all_method_returns_dict(self):
        """Test if the 'all' method returns a dictionary"""
        result = models.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method_adds_to_objects(self):
        """Test if the 'new' method adds to the objects dictionary"""
        obj = BaseModel()
        models.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, models.storage.all().keys())

   
if __name__ == "__main__":
    unittest.main()
