import os
import unittest
from code.hw2 import Supressor, suppressor_gen


class TestSupressor(unittest.TestCase):
    
    def test_supressor(self):
        with Supressor(IndexError):
            self.assertRaises(IndexError, lambda: [][2])

    def test_supressor_gen(self):
        with suppressor_gen(IndexError):
            self.assertRaises(IndexError, lambda: [][2])

if __name__ == '__main__':
    unittest.main()