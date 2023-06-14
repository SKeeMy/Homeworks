import unittest
import os
from importlib.machinery import SourceFileLoader

task2_path = 'C:\\Users\\SKeeMy\\Desktop\\Python\\tasks\\homework_3\\code\\task2.py'
task2 = SourceFileLoader('task2', task2_path).load_module()


class TestIsArmstrongNumber(unittest.TestCase):

    def test_is_armstrong_number_true(self):
        self.assertTrue(task2.is_armstrong_number(153))
        self.assertTrue(task2.is_armstrong_number(9474))
        self.assertTrue(task2.is_armstrong_number(54748))

    def test_is_armstrong_number_false(self):
        self.assertFalse(task2.is_armstrong_number(-153))
        self.assertFalse(task2.is_armstrong_number(12))
        self.assertFalse(task2.is_armstrong_number(100))
        self.assertFalse(task2.is_armstrong_number('153'))

    def test_is_armstrong_number_type_error(self):
        with self.assertRaises(TypeError):
            task2.is_armstrong_number('abc')


if __name__ == '__main__':
    unittest.main()
