#!/usr/bin/python3
# test_base.py
"""Module defines test class for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


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

class TestCreateMethod(unittest.TestCase):

    def test_create_rectangle_with_valid_dict(self):
        dictionary = {'width': 4, 'height': 5}
        instance = Rectangle.create(**dictionary)
        self.assertEqual(instance.width, 4)
        self.assertEqual(instance.height, 5)

    def test_create_square_with_valid_dict(self):
        dictionary = {'size': 4}
        instance = Square.create(**dictionary)
        self.assertEqual(instance.size, 4)

    def test_create_with_invalid_dict_type(self):
        dictionary = 'not a dict'
        with self.assertRaises(TypeError):
            Rectangle.create(**dictionary)

    def test_create_rectangle_with_missing_key(self):
        dictionary = {'width': 4}
        instance = Rectangle.create(**dictionary)
        self.assertEqual(instance.width, 4)
        self.assertEqual(instance.height, 3)  # Default value

    def test_create_square_with_missing_key(self):
        dictionary = {}
        instance = Square.create(**dictionary)
        self.assertEqual(instance.size, 2)  # Default value

    def test_create_rectangle_with_extra_key(self):
        dictionary = {'width': 4, 'height': 5, 'extra': 'key'}
        instance = Rectangle.create(**dictionary)
        self.assertEqual(instance.width, 4)
        self.assertEqual(instance.height, 5)

    def test_create_square_with_extra_key(self):
        dictionary = {'size': 4, 'extra': 'key'}
        instance = Square.create(**dictionary)
        self.assertEqual(instance.size, 4)

    def test_create_rectangle_with_invalid_key(self):
        dictionary = {'invalid_key': 4, 'height': 5}
        instance = Rectangle.create(**dictionary)
        self.assertEqual(instance.width, 2)  # Default value
        self.assertEqual(instance.height, 5)

    def test_create_square_with_invalid_key(self):
        dictionary = {'invalid_key': 4}
        instance = Square.create(**dictionary)
        self.assertEqual(instance.size, 2)  # Default value

class TestLoadFromFile(unittest.TestCase):

    def test_load_from_file_non_existent_file(self):
        # Test loading from a non-existent file
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_empty_file(self):
        # Test loading from an empty file
        with open('Square.json', 'w') as file:
            file.write('')
        self.assertEqual(Square.load_from_file(), [])
        os.remove('Square.json')

    def test_load_from_file_valid_json(self):
        # Test loading from a file with valid JSON content
        with open('Rectangle.json', 'w') as file:
            file.write('[{"key": "value"}]')
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 1)
        self.assertIsInstance(instances[0], Rectangle)
        os.remove('Rectangle.json')

    def test_load_from_file_invalid_json(self):
        # Test loading from a file with invalid JSON content
        with open('Square.json', 'w') as file:
            file.write('Invalid JSON')
        with self.assertRaises(TypeError):
            Square.load_from_file()
        os.remove('Square.json')

class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)
