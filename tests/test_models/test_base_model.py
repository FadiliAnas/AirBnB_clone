#!/usr/bin/python3
"""
Tests for BaseModel
"""
import unittest
from datetime import datetime, timedelta
from models import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

        def test_init(self):
            self.assertIsNotNone(self.base_model.id)
            self.assertIsInstance(self.base_model.created_at, datetime)
            self.assertIsInstance(self.base_model.updated_at, datetime)

        def test_str(self):
            expected_str = f"[{self.base_model.__class__.__name__}] ({self.base_model.id}) {self.base_model.__dict__}"
            self.assertEqual(str(self.base_model), expected_str)

        def test_save(self):
            old_updated_at = self.base_model.updated_at
            self.base_model.save()
            self.assertNotEqual(old_updated_at, self.base_model.updated_at)

        def test_to_dict(self):
            obj_dict = self.base_model.to_dict()
            self.assertIsInstance(obj_dict, dict)
            self.assertIn('id', obj_dict)
            self.assertIn('__class__', obj_dict)
            self.assertIn('created_at', obj_dict)
            self.assertIn('updated_at', obj_dict)
            self.assertEqual(obj_dict['id'], self.base_model.id)
            self.assertEqual(obj_dict['__class__'], self.base_model.__class__.__name__)
            self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
            self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

        def test_init_with_kwargs(self):
            test_id = "test_id"
            created_at = datetime.now() - timedelta(days=1)
            updated_at = datetime.now() - timedelta(hours=1)
            kwargs = {
                'id': test_id,
                'created_at': created_at.isoformat(),
                'updated_at': updated_at.isoformat()
            }
            base_model = BaseModel(**kwargs)
            self.assertEqual(base_model.id, test_id)
            self.assertEqual(base_model.created_at, created_at)
            self.assertEqual(base_model.updated_at, updated_at)

if __name__ == '__main__':
    unittest.main()
