#!/usr/bin/python3
"""
Test of the max integer module

This test case ensures the max integer function handles
type checks when computing the correct answer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test the max_integer function
    """

    def test_max_integer(self):
        '''
        Test if integer is max integer


        '''
        result = max_integer([1, 4, 3, 2])
        self.assertEqual(result, 4)
        result = max_integer([12, 9, 7, 2])
        self.assertEqual(result, 12)
        result = max_integer([1])
        self.assertEqual(result, 1)
        result = max_integer()
        self.assertEqual(result, None)

    def test_isint(self):
        '''
        Test to check variable against integer


        '''
        var = 1
        self.assertTrue(max_integer([var, 2]) == 2)
        x = 5
        self.assertTrue(max_integer([1, x]) == x)

    def test_float_integer(self):
        '''
        Test to see if float is max integer


        '''
        self.assertEqual(max_integer([4.0, 3, 2]), 4.0)

    def test_negative_integer(self):
        '''
        Test only negative integers


        '''
        self.assertEqual(max_integer([-1, -2, -5]), -1)

    if __name__ == '__main__':
        unittest.main()
