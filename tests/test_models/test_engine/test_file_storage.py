#!/usr/bin/python3
"""
Test of file Storage
"""
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
        setattr(self.storage, "_FileStorage__objects", {})
        self.file_path = models.storage._FileStorage__file_path
        self.instance = BaseModel()
        self.objs = models.storage._FileStorage__objects
        self.keyname = f"BaseModel.{self.instance.id}"

    def test_all_method_exists(self):
        """Test if the 'all' method exists"""
        self.assertTrue(hasattr(models.storage, "all"))

    def test_new_method_exists(self):
        """Test if the 'new' method exists"""
        self.assertTrue(hasattr(models.storage, "new"))

        expected_data = {key: value.to_dict() for key,
                         value in self.objs.items()}
        self.assertEqual(saved_data, expected_data)


if __name__ == "__main__":
    unittest.main()
