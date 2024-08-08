#!/usr/bin/python3
# test_rectangle.py
"""Test the rectangle class"""
import unittest
from models.rectangle import Rectangle, Base


class TestRectangle_Instantiation(unittest.TestCase):

    def test_Rectangle_instance(self):
        self.assertIsInstance(Rectangle(10, 20), Base)

    def test_0_args(self):
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_1_args(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10)

    def test_2_args(self):
        rect = Rectangle(10, 20)

        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 1)

    def test_3_args(self):
        rect = Rectangle(10, 20, 5)

        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 2)

    def test_4_args(self):
        rect = Rectangle(10, 20, 5, 7)

        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 7)
        self.assertEqual(rect.id, 3)

    def test_5_args(self):
        rect = Rectangle(10, 20, 5, 7, 49)

        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 7)
        self.assertEqual(rect.id, 49)

    def test_excess_args(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(*(range(10)))

    def test_private_width(self):
        rect = Rectangle(10, 20, 5, 7, 49)

        with self.assertRaises(AttributeError):
            print(rect.__width)

    def test_private_height(self):
        rect = Rectangle(10, 20, 5, 7, 49)

        with self.assertRaises(AttributeError):
            print(rect.__height)

    def test_private_x(self):
        rect = Rectangle(10, 20, 5, 7, 49)

        with self.assertRaises(AttributeError):
            print(rect.__x)

    def test_private_y(self):
        rect = Rectangle(10, 20, 5, 7, 49)

        with self.assertRaises(AttributeError):
            print(rect.__y)

class TestRectangle_width_validation(unittest.TestCase):

    def test_neg_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-10, 20)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 20)

    def test_width_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("Hello", 20)

class TestRectangle_height_validation(unittest.TestCase):

    def test_neg_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, -20)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 0)

    def test_height_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(45, "PiedPiper")

class TestRectangle_x_validation(unittest.TestCase):

    def test_neg_x(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 20, -5)

    def test_x_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 20, (34, 43))

class TestRectangle_y_validation(unittest.TestCase):

    def test_neg_y(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 20, 5, -25)

    def test_y_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 20, 34, ["One", "Two", "Three"])
