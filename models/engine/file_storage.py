import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up for testing"""
        self.test_storage = storage.FileStorage()

    def tearDown(self):
        """Tear down after testing"""
        try:
            os.remove(storage.FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all method"""
        all_objs = self.test_storage.all()
        self.assertEqual(type(all_objs), dict)
        self.assertIs(all_objs, self.test_storage._FileStorage__objects)

    def test_new(self):
        """Test new method"""
        new_user = User()
        self.test_storage.new(new_user)
        key = "{}.{}".format(new_user.__class__.__name__, new_user.id)
        self.assertIn(key, self.test_storage._FileStorage__objects)

    def test_save(self):
        """Test save method"""
        new_user = User()
        self.test_storage.new(new_user)
        self.test_storage.save()
        with open(storage.FileStorage._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertIn(new_user.__class__.__name__, data)
            self.assertIn(new_user.id, data)

    def test_reload(self):
        """Test reload method"""
        new_user = User()
        self.test_storage.new(new_user)
        self.test_storage.save()
        self.test_storage.reload()
        key = "{}.{}".format(new_user.__class__.__name__, new_user.id)
        self.assertIn(key, self.test_storage._FileStorage__objects)
        self.assertEqual(self.test_storage._FileStorage__objects[key].to_dict(), new_user.to_dict())


if __name__ == '__main__':
    unittest.main()
