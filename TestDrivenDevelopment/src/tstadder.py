"""Demonstrates the value of test driven programming"""
from adder import adder
import unittest

class TestAddr(unittest.TestCase):

    def test_num(self):
        self.assertEqual(adder(3,4), 7, "3 + 4 should 7")

    def test_string(self):
        self.assertEqual(adder('x','y'), 'xy', "x + y should be xy")

    def test_list(self):
        self.assertEqual(adder([1,2,3],[4,5]), [1,2,3,4,5], " list addition failing")

    def test_num_string(self):
        self.assertEqual(adder(4,'x'),'4x', "4 +x is 4x")

    def test_num_list(self):
        self.assertEqual(adder(4, [1,2]), [1,2,4], "num list is failing")

if __name__ == "__main__":
    unittest.main()
