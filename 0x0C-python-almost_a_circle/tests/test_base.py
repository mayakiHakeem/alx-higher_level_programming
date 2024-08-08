#!/usr/bin/python3
# test_base.py
"""Module defines test class for base.py"""
import unittest
from models.base import Base

class TestBase_Instantiation(unittest.TestCase):
    """Test instantiation of the Base class.
    """
    # test initialization with id set
    def test_init_with_id(self):
        b4 = Base(12)
        b6 = Base("Hooli")
        b7 = Base({'a': 1, 'b': 2, 'c': 3})

        self.assertEqual(b4.id, 12)
        self.assertEqual(b6.id, "Hooli")
        self.assertEqual(b7.id, {'a': 1, 'b': 2, 'c': 3})

    # test initialization without id
    def test_init_without_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b3.id, 3)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b1.id, b2.id - 1)

    # test for initialization with more than one argument
    def test_init_large_args(self):
        self.assertRaises(TypeError, Base, *(range(10)))

    #
