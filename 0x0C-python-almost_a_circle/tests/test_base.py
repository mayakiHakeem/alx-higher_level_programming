#!/usr/bin/python3
# test_base.py
"""Module defines test class for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

class TestSaveToFile(unittest.TestCase):

    def test_saving_list_of_rectangle_instances(self):
        # Create a list of Rectangle instances
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(3, 4)
        list_rects = [rect1, rect2]

        # Call save_to_file
        Rectangle.save_to_file(list_rects)

        # Verify file contents
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(contents, Rectangle.to_json_string([rect1.to_dictionary(), rect2.to_dictionary()]))

    def test_saving_list_of_square_instances(self):
        # Create a list of Square instances
        sq1 = Square(5)
        sq2 = Square(6)
        list_squares = [sq1, sq2]

        # Call save_to_file
        Square.save_to_file(list_squares)

        # Verify file contents
        with open("Square.json", "r") as file:
            contents = file.read()
            self.assertEqual(contents, Square.to_json_string([sq1.to_dictionary(), sq2.to_dictionary()]))

    def test_saving_none(self):
        # Call save_to_file with None
        Rectangle.save_to_file(None)

        # Verify file contents
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(contents, "[]")

    def test_overwriting_file(self):
        # Create a list of Rectangle instances
        rect1 = Rectangle(1, 2)
        list_rects = [rect1]

        # Call save_to_file
        Rectangle.save_to_file(list_rects)

        # Verify file contents
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(contents, Rectangle.to_json_string([rect1.to_dictionary()]))

        # Create another list of Rectangle instances
        rect2 = Rectangle(3, 4)
        list_rects = [rect2]

        # Call save_to_file again
        Rectangle.save_to_file(list_rects)

        # Verify file contents are overwritten
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(contents, Rectangle.to_json_string([rect2.to_dictionary()]))

    def test_non_list_arg_passed_to_save_to_file(self):
        # Call save_to_file with a non-list argument
        with self.assertRaises(TypeError):
            Rectangle.save_to_file("string")

    def test_list_doesnt_contain_all_sub_instances_of_base(self):
        # Create a list with non-Base objects
        list_objs = [1, "string", Rectangle(1, 2)]

        # Call save_to_file and verify TypeError is raised
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(list_objs)

    def test_list_contains_mixed_sub_instances_of_base(self):
        # Create a list with mixed sub-instances of Base
        list_objs = [Rectangle(1, 2), Square(3)]

        # Call save_to_file and verify TypeError is raised
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(list_objs)

class TestFromJsonString(unittest.TestCase):

    def test_valid_json_string(self):
        json_string = '[{"key": "value"}, {"key2": "value2"}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [{'key': 'value'}, {'key2': 'value2'}])

    def test_empty_json_string(self):
        json_string = ''
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_none_json_string(self):
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_invalid_json_string(self):
        json_string = '[{"key": "value" '
        with self.assertRaises(TypeError):
            Base.from_json_string(json_string)

    def test_json_string_with_trailing_comma(self):
        json_string = '[{"key": "value"}, ]'
        with self.assertRaises(TypeError):
            Base.from_json_string(json_string)

    def test_json_string_with_comment(self):
        json_string = '[{"key": "value"} // comment]'
        with self.assertRaises(TypeError):
            Base.from_json_string(json_string)
