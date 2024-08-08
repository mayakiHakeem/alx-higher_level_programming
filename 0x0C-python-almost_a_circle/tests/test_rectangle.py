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
        self.assertEqual(rect.id, 1)

    def test_4_args(self):
        rect = Rectangle(10, 20, 5, 7)

        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 7)
        self.assertEqual(rect.id, 1)

    def test_5_args(self):
        rect = Rectangle(10, 20, 5, 7, 49)

        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 7)
        self.assertEqual(rect.id, 49)

    def test_excess_args(self):
        with self.assertEqual(TypeError):
            rect = Rectangle(*(range(10)))

    def test_private_width(self):
        rect = Rectangle(10, 20, 5, 7, 49)

        with self.assertEqual(TypeError):
            print(rect.__width)

    def test_private_height(self):
        rect = Rectangle(10, 20, 5, 7, 49)

        with self.assertEqual(TypeError):
            print(rect.__height)

    def test_private_x(self):
        rect = Rectangle(10, 20, 5, 7, 49)

        with self.assertEqual(TypeError):
            print(rect.__x)

    def test_private_y(self):
        rect = Rectangle(10, 20, 5, 7, 49)

        with self.assertEqual(TypeError):
            print(rect.__y)
