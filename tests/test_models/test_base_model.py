import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage"""

    def setUp(self):
        """Set up the test cases"""
        self.file_path = storage._FileStorage__file_path
        self.instance = BaseModel()
        self.objs = storage._FileStorage__objects
        self.keyname = f"BaseModel.{self.instance.id}"

    def test_all_method_exists(self):
        """Test if the 'all' method exists"""
        self.assertTrue(hasattr(storage, "all"))

    def test_new_method_exists(self):
        """Test if the 'new' method exists"""
        self.assertTrue(hasattr(storage, "new"))

    def test_reload_method_exists(self):
        """Test if the 'reload' method exists"""
        self.assertTrue(hasattr(storage, "reload"))

    def test_all_method_returns_dict(self):
        """Test if the 'all' method returns a dictionary"""
        result = storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method_adds_to_objects(self):
        """Test if the 'new' method adds to the objects dictionary"""
        obj = BaseModel()
        storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, storage.all().keys())

    def test_save_method_saves_to_file(self):
        """Test if the 'save' method saves to the file"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        storage.save()

        with open(self.file_path, "r") as data_file:
            saved_data = json.load(data_file)

        expected_data = {key: value.to_dict() for key, value in self.objs.items()}
        self.assertEqual(saved_data, expected_data)


if __name__ == "__main__":
    unittest.main()
