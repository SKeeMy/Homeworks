import unittest
import os
from multiprocessing import Pool
from importlib.machinery import SourceFileLoader

task2_path = 'C:\\Users\\SKeeMy\\Desktop\\Python\\tasks\\homework_3\\code\\task2.py'
task2 = SourceFileLoader('task2', task2_path).load_module()


class TestSlowCalculate(unittest.TestCase):

    def test_slow_calculate(self):
        with Pool() as pool:
            values = range(501)
            results = pool.map(task2.slow_calculate, values)
            total_sum = sum(results)
            self.assertIsInstance(total_sum, int)


if __name__ == '__main__':
    unittest.main()
