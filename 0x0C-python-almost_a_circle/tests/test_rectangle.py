#!/usr/bin/python3
# test_rectangle.py
"""Test the rectangle class"""
import unittest
from models.rectangle import Rectangle, Base
import io
from unittest.mock import patch


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
        r = Rectangle(10, 20)
        r1 = Rectangle(5, 15)

        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, r1.id - 1)

    def test_3_args(self):
        rect = Rectangle(10, 20, 5)
        rect1 = Rectangle(5, 15, 3)

        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, rect1.id - 1)

    def test_4_args(self):
        rect2 = Rectangle(10, 20, 5, 7)
        rect3 = Rectangle(5, 15, 3, 5)

        self.assertEqual(rect2.width, 10)
        self.assertEqual(rect2.height, 20)
        self.assertEqual(rect2.x, 5)
        self.assertEqual(rect2.y, 7)
        self.assertEqual(rect2.id, rect3.id -1)

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

class TestRectangle_Area(unittest.TestCase):

    def test_area_valid(self):
        rect = Rectangle(10, 20)
        self.assertEqual(rect.area(), 200)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 20)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 0)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-10, 20)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, -20)

    def test_width_not_int(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("Python", 20)

    def test_height_not_int(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, "C is fun")

    def test_area_0_attr_rect(self):
        with self.assertRaises(TypeError):
            rect7 = Rectangle()

    def test_area_1_attr_rect(self):
        with self.assertRaises(TypeError):
            rect7 = Rectangle(4)

    def test_area_excess_attrs(self):
        with self.assertRaises(TypeError):
            rect7 = Rectangle(*(range(5, 11)))

class TestRectangle_Display(unittest.TestCase):

    def test_display_valid(self):
        r6 = Rectangle(4, 3)
        with patch("sys.stdout", new=io.StringIO()) as displayed_output:
            r6.display()
            self.assertEqual(displayed_output.getvalue(), "####\n####\n####\n")

    def test_negative_width_display(self):
        with self.assertRaises(ValueError):
            r7 = Rectangle(-4, 3)

    def test_zero_width_display(self):
        with self.assertRaises(ValueError):
            r8 = Rectangle(0, 3)

    def test_display_width_not_int(self):
        with self.assertRaises(TypeError):
            r9 = Rectangle("Name", 3)

    def test_negative_height_display(self):
        with self.assertRaises(ValueError):
            r7 = Rectangle(4, -3)

    def test_zero_height_display(self):
        with self.assertRaises(ValueError):
            r8 = Rectangle(10, 0)

    def test_display_width_not_int(self):
        with self.assertRaises(TypeError):
            r9 = Rectangle(4, "3")

    def test_display_0_attr_rect(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle()

    def test_display_1_attr(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle(4)

    def test_display_excess_attrs(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle(*(range(5, 11)))

    def test_display_valid_x(self):
        rect = Rectangle(3, 2, 2)
        with patch("sys.stdout", new=io.StringIO()) as displayed_out:
            rect.display()
            self.assertEqual(displayed_out.getvalue(), "  ###\n  ###\n")

    def test_display_valid_x_y(self):
        rect1 = Rectangle(3, 2, 2, 1)
        with patch("sys.stdout", new=io.StringIO()) as displayed_out:
            rect1.display()
            self.assertEqual(displayed_out.getvalue(), "\n  ###\n  ###\n")

    def test_display_valid_y_x_0(self):
        rect = Rectangle(3, 2, 0, 2)
        with patch("sys.stdout", new=io.StringIO()) as displayed_out:
            rect.display()
            self.assertEqual(displayed_out.getvalue(), "\n\n###\n###\n")

    def test_display_negative_x(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(3, 2, -2, 4)

    def test_display_negative_y(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(3, 2, 2, -4)

    def test_display_x_not_int(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 2, "Hi", 4)

    def test_display_y_not_int(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 2, 2, "Hello")

    def test_display_valid_x_y_id(self):
        rect1 = Rectangle(3, 2, 2, 1, 28)
        with patch("sys.stdout", new=io.StringIO()) as displayed_out:
            rect1.display()
            self.assertEqual(displayed_out.getvalue(), "\n  ###\n  ###\n")
            self.assertEqual(rect1.id, 28)

class TestRectangle_str_rep(unittest.TestCase):

    def test_valid_str_rep_2(self):
        r6 = Rectangle(4, 3)
        self.assertEqual(str(r6), f"[Rectangle] ({r6.id}) 0/0 - 4/3")

    def test_valid_str_rep_3(self):
        r6 = Rectangle(4, 3, 2)
        self.assertEqual(str(r6), f"[Rectangle] ({r6.id}) 2/0 - 4/3")

    def test_valid_str_rep_4(self):
        r6 = Rectangle(4, 3, 2, 7)
        self.assertEqual(str(r6), f"[Rectangle] ({r6.id}) 2/7 - 4/3")

    def test_valid_str_rep_5(self):
        r6 = Rectangle(4, 3, 2, 7, 32)
        self.assertEqual(str(r6), f"[Rectangle] ({r6.id}) 2/7 - 4/3")

    def test_negative_width_str_rep(self):
        with self.assertRaises(ValueError):
            r7 = Rectangle(-4, 3)

    def test_zero_width_str_rep(self):
        with self.assertRaises(ValueError):
            r8 = Rectangle(0, 3)

    def test_str_rep_width_not_int(self):
        with self.assertRaises(TypeError):
            r9 = Rectangle("Name", 3)

    def test_negative_height_str_rep(self):
        with self.assertRaises(ValueError):
            r7 = Rectangle(4, -3)

    def test_zero_height_str_rep(self):
        with self.assertRaises(ValueError):
            r8 = Rectangle(10, 0)

    def test_str_rep_width_not_int(self):
        with self.assertRaises(TypeError):
            r9 = Rectangle(4, "3")

    def test_str_rep_0_attr_rect(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle()

    def test_str_rep_1_attr(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle(4)

    def test_str_rep_excess_attrs(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle(*(range(5, 11)))

class TestRectangle_Update(unittest.TestCase):

    def test_update_0_arg(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/10 - 10/10")

    def test_update_1_arg(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/10 - 10/10")

    def test_update_2_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/10 - 2/10")

    def test_update_3_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/10 - 2/3")

    def test_update_4_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 4/10 - 2/3")

    def test_update_5_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 4/5 - 2/3")

    def test_update_excess_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(*(range(5, 12)))

    def test_update_non_int_2nd_arg(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(23, "Hello")

    def test_update_non_int_3rd_arg(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(2, 4, "Hello")

    def test_update_non_int_4th_arg(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(2, 4, 6, "Hello")

    def test_update_non_int_5th_arg(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(2, 4, 6, 8, "Hello")

    def test_update_zero_width(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r1.update(2, 0)

    def test_update_zero_height(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r1.update(2, 4, 0)

    def test_update_negative_width(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r1.update(2, -5)

    def test_update_negative_height(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r1.update(2, 4, -5)

    def test_update_negative_x(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r1.update(2, 3, 4, -2)

    def test_update_negative_y(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r1.update(2, 4, 6, 8, -10)

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=20, width=30)
        self.assertEqual(r1.id, 20)
        self.assertEqual(r1.width, 30)

    def test_update_args_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(20, 30, height=40, y=50)
        self.assertEqual(r1.id, 20)
        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 40)
        self.assertEqual(r1.y, 50)

    def test_update_args_skip_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(20, 30, 40, 50, id=60)
        self.assertEqual(r1.id, 20)
        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 40)
        self.assertEqual(r1.x, 50)
