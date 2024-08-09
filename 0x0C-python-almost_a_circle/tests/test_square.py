#!/usr/bin/python3
# test_square.py
"""Test the square class"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import io
from unittest.mock import patch


class TestSquare_Instantiation(unittest.TestCase):

    def test_Square_as_Base_instance(self):
        self.assertIsInstance(Square(10), Base)

    def test_Square_as_Rectangle_instance(self):
        self.assertIsInstance(Square(10), Rectangle)

    def test_0_args(self):
        with self.assertRaises(TypeError):
            square = Square()

    def test_1_args(self):
        sq = Square(10)
        sq1 = Square(5)

        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, sq1.id - 1)

    def test_2_args(self):
        sq = Square(10, 20)
        sq1 = Square(5, 15)

        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.x, 20)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, sq1.id - 1)

    def test_3_args(self):
        sq2 = Square(10, 20, 5)
        sq3 = Square(5, 15, 3)

        self.assertEqual(sq2.size, 10)
        self.assertEqual(sq2.x, 20)
        self.assertEqual(sq2.y, 5)
        self.assertEqual(sq2.id, sq3.id -1)

    def test_4_args(self):
        sq4 = Square(10, 20, 5, 7)

        self.assertEqual(sq4.size, 10)
        self.assertEqual(sq4.x, 20)
        self.assertEqual(sq4.y, 5)
        self.assertEqual(sq4.id, 7)

    def test_excess_args(self):
        with self.assertRaises(TypeError):
            sqx = Square(*(range(10)))

    def test_private_width(self):
        sq5 = Square(20, 5, 7, 49)
        with self.assertRaises(AttributeError):
            print(sq5.__width)

    def test_private_height(self):
        sq6 = Square(10, 5, 7, 49)
        with self.assertRaises(AttributeError):
            print(sq6.__height)

    def test_private_x(self):
        sq7 = Square(10, 5, 7, 49)
        with self.assertRaises(AttributeError):
            print(sq7.__x)

    def test_private_y(self):
        sq8 = Square(10, 5, 7, 49)
        with self.assertRaises(AttributeError):
            print(sq8.__y)


class TestSquare_size_validation(unittest.TestCase):

    def test_neg_size(self):
        with self.assertRaises(ValueError):
            sq = Square(-10)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            sq1 = Square(0)

    def test_size_type(self):
        with self.assertRaises(TypeError):
            sq2 = Square("Hello")

class TestSquare_x_validation(unittest.TestCase):

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            sq = Square(10, -5)

    def test_x_type(self):
        with self.assertRaises(TypeError):
            sq1 = Square(10, (34, 43))

class TestSquare_y_validation(unittest.TestCase):

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            sq = Square(10, 5, -25)

    def test_y_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 34, ["One", "Two", "Three"])

class TestRectangle_str_rep(unittest.TestCase):

    def test_valid_str_rep_1(self):
        sq = Square(4)
        self.assertEqual(str(sq), f"[Square] ({sq.id}) 0/0 - 4")

    def test_valid_str_rep_2(self):
        sq1 = Square(4, 3)
        self.assertEqual(str(sq1), f"[Square] ({sq1.id}) 3/0 - 4")

    def test_valid_str_rep_3(self):
        sq2 = Square(4, 3, 2)
        self.assertEqual(str(sq2), f"[Square] ({sq2.id}) 3/2 - 4")

    def test_valid_str_rep_4(self):
        sq3 = Square(4, 3, 2, 8)
        self.assertEqual(str(sq3), f"[Square] ({sq3.id}) 3/2 - 4")

    def test_negative_size_str_rep(self):
        with self.assertRaises(ValueError):
            sq4 = Square(-4)

    def test_zero_size_str_rep(self):
        with self.assertRaises(ValueError):
            sq5 = Square(0)

    def test_str_rep_size_not_int(self):
        with self.assertRaises(TypeError):
            sq6 = Square("Name")

    def test_str_rep_0_attr_rect(self):
        with self.assertRaises(TypeError):
            sq7 = Square()

    def test_str_rep_excess_attrs(self):
        with self.assertRaises(TypeError):
            sq = Square(*(range(5, 10)))

    def test_negative_x_str_rep(self):
        with self.assertRaises(ValueError):
            sq4 = Square(5, -4)

    def test_str_rep_x_not_int(self):
        with self.assertRaises(TypeError):
            sq6 = Square(5, "Name")

    def test_negative_y_str_rep(self):
        with self.assertRaises(ValueError):
            sq4 = Square(5, 4, -4)

    def test_str_rep_y_not_int(self):
        with self.assertRaises(TypeError):
            sq6 = Square(5, 4, "Name")

class TestSquare_size_validation(unittest.TestCase):

    def test_neg_size(self):
        with self.assertRaises(ValueError):
            sq = Square(-10)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            sq1 = Square(0)

    def test_size_type(self):
        with self.assertRaises(TypeError):
            sq2 = Square("Hello")

class TestSquare_Update(unittest.TestCase):

    def test_sq_update_0_arg(self):
        sq1 = Square(10, 10, 10)
        sq1.update()
        self.assertEqual(str(sq1), f"[Square] ({sq1.id}) 10/10 - 10")

    def test_sq_update_1_arg(self):
        sq1 = Square(10, 10, 10)
        sq1.update(89)
        self.assertEqual(str(sq1), f"[Square] ({sq1.id}) 10/10 - 10")

    def test_sq_update_2_args(self):
        sq1 = Square(10, 10, 10)
        sq1.update(89, 2)
        self.assertEqual(str(sq1), f"[Square] ({sq1.id}) 10/10 - 2")

    def test_sq_update_3_args(self):
        sq1 = Square(10, 10, 10)
        sq1.update(89, 2, 3)
        self.assertEqual(str(sq1), f"[Square] ({sq1.id}) 3/10 - 2")

    def test_sq_update_4_args(self):
        sq1 = Square(10, 10, 10)
        sq1.update(89, 2, 3, 4)
        self.assertEqual(str(sq1), f"[Square] ({sq1.id}) 3/4 - 2")

    def test_sq_update_excess_args(self):
        sq1 = Square(10, 10, 10)
        with self.assertRaises(TypeError):
            sq1.update(*(range(5, 12)))

    def test_sq_update_non_int_2nd_arg(self):
        sq1 = Square(10, 10, 10)
        with self.assertRaises(TypeError):
            sq1.update(23, "Hello")

    def test_sq_update_non_int_3rd_arg(self):
        sq1 = Square(10, 10, 10)
        with self.assertRaises(TypeError):
            sq1.update(2, 4, "Hello")

    def test_update_non_int_4th_arg(self):
        r1 = Rectangle(10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(2, 4, 6, "Hello")

    def test_sq_update_zero_size(self):
        sq2 = Square(10, 10, 10)
        with self.assertRaises(ValueError):
            sq2.update(2, 0)

    def test_sq_update_negative_size(self):
        sq2 = Square(10, 10, 10)
        with self.assertRaises(ValueError):
            sq2.update(2, -5)

    def test_sq_update_negative_x(self):
        sq2 = Square(10, 10, 10)
        with self.assertRaises(ValueError):
            sq2.update(2, 4, -2)

    def test_sq_update_negative_y(self):
        sq2 = Square(10, 10, 10)
        with self.assertRaises(ValueError):
            sq2.update(2, 4, 8, -10)

    def test_sq_update_kwargs(self):
        sq3 = Square(10, 10, 10)
        sq3.update(id=20, size=30)
        self.assertEqual(sq3.id, 20)
        self.assertEqual(sq3.size, 30)

    def test_sq_update_args_kwargs(self):
        sq4 = Square(10, 10, 10)
        sq4.update(20, size=40, y=50)
        self.assertEqual(sq4.id, 20)
        self.assertEqual(sq4.size, 40)
        self.assertEqual(sq4.x, 10)
        self.assertEqual(sq4.y, 50)

    def test_sq_update_args_skip_kwargs(self):
        sq5 = Square(10, 10, 10)
        sq5.update(20, 40, 50, id=60)
        self.assertEqual(sq5.id, 20)
        self.assertEqual(sq5.size, 40)
        self.assertEqual(sq5.x, 50)
        self.assertEqual(sq5.y, 10)

class TestSquare_to_dictionary(unittest.TestCase):

    def test_dict_instance(self):
        s4 = Square(10, 20, 30, 40)
        dict_rep = s4.to_dictionary()
        self.assertIsInstance(dict_rep, dict)

    def test_dict_valid(self):
        s1 = Square(5)
        dict_rep = s1.to_dictionary()
        self.assertEqual(dict_rep, (
            {'id': int(f"{s1.id}"), 'size': 5, 'x': 0, 'y': 0})
                         )

    def test_dict_unpacking(self):
        s1 = Square(10, 2, 1, 9)
        s1_dict = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dict)
        self.assertFalse(s1 == s2)

    def test_dict_with_excess_args(self):
        with self.assertRaises(TypeError):
            sq = Square(2, 1)
            sq.to_dictionary(1)
