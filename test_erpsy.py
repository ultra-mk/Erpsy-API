import unittest
import os
import json
from app import create_app
from flask_pymongo import MongoClient


class ErpsyTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.part = {"part_name": "Polystyrene PWB",
                     "description": "DC Block Type Reference 22320f",
                     "part_number": "30758314"}

        mongo = MongoClient('localhost', 27017)
        db = mongo['test']
        collection = db['parts']

        collection.insert_one(self.part)

    def test_stuff(self):
        res = self.client().get('/parts/')
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
