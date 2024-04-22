#!/usr/bin/python3
""" Unittest for max_integer([..])
"""


import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """ A module that test for max_integer
            If nothing is supplied return None
    """
    __test_cases = [
            [1, 2, 3, 4],
            [1, 3, 4, 2],
            [],
            [4.5, 2.4, 5.1, 3.0],
            ['a', 'b', 'c', 'd']
        ]
    def test_max_integer(self):
        cases = [4, 4, None, 5.1, 'd']
        for i in range(len(self.__test_cases)):
            self.assertEqual(max_integer(self.__test_cases[i]), cases[i])



if __name__ == '__main__':
    unittest.main()
