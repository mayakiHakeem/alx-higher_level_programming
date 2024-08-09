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
