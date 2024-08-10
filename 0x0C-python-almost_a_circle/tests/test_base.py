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

class TestToJsonString(unittest.TestCase):

    def test_single_list_1_dictionary(self):
        dictionary = {'name': 'John', 'age': 30}
        expected_json = '[{"name": "John", "age": 30}]'
        self.assertEqual(Base.to_json_string([dictionary]), expected_json)

    def test_list_of_dictionaries(self):
        dictionaries = [{'name': 'Joe', 'age': 7}, {'name': 'Ann', 'age': 9}]
        expected_json = '[{"name": "Joe", "age": 7}, {"name": "Ann", "age": 9}]'
        self.assertEqual(Base.to_json_string(dictionaries), expected_json)

    def test_empty_list(self):
        dictionaries = []
        expected_json = '[]'
        self.assertEqual(Base.to_json_string(dictionaries), expected_json)

    def test_non_list_of_dictionary_input_str(self):
        string = "Hello, Guys"
        with self.assertRaises(TypeError):
            Base.to_json_string(string)

    def test_non_list_of_dictionary_int_input(self):
        number = 57
        with self.assertRaises(TypeError):
            Base.to_json_string(number)

    def test_non_list_of_dictionary_dict_input(self):
        dictionary = {'name': 'John', 'is_student': True}
        with self.assertRaises(TypeError):
            Base.to_json_string(dictionary)

    def test_list_with_non_dict_input(self):
        list_with_non_dict = [{'name': 'John'}, 'not a dict']
        with self.assertRaises(TypeError):
            Base.to_json_string(list_with_non_dict)

    def test_nested_dictionaries(self):
        dictionary = {'name': 'Jo', 'ad': {'st': '32 Rd', 'city': 'DC'}}
        expected_json = '[{"name": "Jo", "ad": {"st": "32 Rd", "city": "DC"}}]'
        self.assertEqual(Base.to_json_string([dictionary]), expected_json)

    def test_different_data_types(self):
        dictionary = {'name': 'John', 'is_student': True, 'height': 1.75}
        expected_json = '[{"name": "John", "is_student": true, "height": 1.75}]'
        self.assertEqual(Base.to_json_string([dictionary]), expected_json)

    def test_excess_inputs(self):
        with self.assertRaises(TypeError):
            dictionary = {'name': 'John', 'is_student': True, 'height': 1.75}
            Base.to_json_string([dictionary], 4)
