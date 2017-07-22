import unittest
from app import create_app
from flask_pymongo import MongoClient
import json


class ErpsyTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.part = {"name": "Polystyrene PWB",
                     "description": "DC Block Type Reference 22320f",
                     "part_number": "30758314"}

        self.mongo = MongoClient('localhost', 27017)
        db = self.mongo['test']
        self.collection = db['parts']
        self.collection.insert_one(self.part)

    def test_parts_response(self):
        res = self.client().get('/parts/')
        self.assertEqual(res.status_code, 200)

    def test_parts_format(self):
        res = self.client().get('/parts/')
        keys = set(json.loads(res.get_data(as_text=True))[
            0].keys())
        self.assertEqual(
            keys, set(['part_number', 'description', 'name']))

    def tearDown(self):
        self.collection.delete_many({})
        self.mongo.close()

if __name__ == '__main__':
    unittest.main()
