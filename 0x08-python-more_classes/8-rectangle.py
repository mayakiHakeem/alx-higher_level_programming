#!/usr/bin/python3
""" A Rectangle class
    Attr:
        width: private attribute of Rectangle class
        height: private attribute of Rectangle class
    Raise:
        TypeError if width and height are not an integer
        ValueError if width and height  are less than zero
"""


class Rectangle:
    """ Class Module below """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ A getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ A method that sets an attribute """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ A getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ A method that sets an attribute """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ A method that find the area of a rectangle """
        return self.width * self.height

    def perimeter(self):
        """ A method that find the perimeter of a rectangle """
        if self.width == 0 or self.height == 0:
            param = 0
        else:
            param = 2 * (self.width + self.height)
        return param

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1.area() < rect_2.area():
                return rect_2
            elif rect_1.area() > rect_2.area():
                return rect_1
            else:
                return rect_1

    def __del__(self):
        """ a method that indicate an instance was deleted """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    def __str__(self):
        """ A print Rectangle class like a text """
        printout = ''
        if (self.height or self.width) == 0:
            printout = ''
        else:
            for _ in range(self.height):
                printout += str(self.print_symbol) * self.width + '\n'
        return printout.rstrip()

    def __repr__(self):
        """ create a new instance """
        return f'Rectangle({self.width}, {self.height})'
