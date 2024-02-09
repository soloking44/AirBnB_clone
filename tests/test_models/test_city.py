#!/usr/bin/python3
""" this test city """

import unittests
import pep8
import os
from models import City
from models.base_model import BaseModel

class Test_City(unittest.TestCase):
    """ this tests city """

    def test_pep8_City(self):
        """this tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")

    def test_City_dict(self):
        """ this city_dict """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)
        self.assertTrue('__class__' in self.city.__dict__)


    def test_save_City(self):
        """ this is save_city """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_inst(self):
        """ this is test_inst"""
        self.assertIsInstance(self.new_city, City)

if __name__ == "__main__":
    unittest.main()
