#!/usr/bin/python3
"""s Module Contains test cases for ClassLoader"""

from helpers.class_loader import ClassLoader
from models.base_model import BaseModel
import unittest

class TestClassLoader(unittest.TestCase):
    """This Class Defines test cases for ClassLoader"""

    def test_load(self):
        """Method should load BaseModel"""
        model = ClassLoader.load("BaseModel")
        self.assertIs(model, BaseModel)

    def test_load_none(self):
        """It should return None"""

        model = ClassLoader.load(None)
        self.assertIsNone(model)

    def test_load_number(self):
        """It should return None"""

        model = ClassLoader.load(101)
        self.assertIsNone(model)
        model = ClassLoader.load(10.1)
        self.assertIsNone(model)

    def test_load_empty_str(self):
        """It should return None"""

        model = ClassLoader.load("")
        self.assertIsNone(model)

    def test_load_not_existing_class(self):
        """It should return None"""

        model = ClassLoader.load("MyModel")
        self.assertIsNone(model)


if __name__ == "__main__":
    unittest.main(TestClassLoader)
