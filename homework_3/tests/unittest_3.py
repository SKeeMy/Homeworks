import unittest
import os
from importlib.machinery import SourceFileLoader

task2_path = 'C:\\Users\\SKeeMy\\Desktop\\Python\\tasks\\homework_3\\code\\task2.py'
task2 = SourceFileLoader('task2', task2_path).load_module()


class TestMakeFilter(unittest.TestCase):

    def test_make_filter_empty(self):
        self.assertEqual(task2.make_filter(), task2.Filter([]))

    def test_make_filter_single_keyword(self):
        expected_filter = task2.Filter([lambda item: item['type'] == 'bird'])
        self.assertEqual(task2.make_filter(type='bird'), expected_filter)

    def test_make_filter_multiple_keywords(self):
        expected_filter = task2.Filter([
            lambda item: item['type'] == 'person',
            lambda item: item['occupation'] == 'was here'
        ])
        self.assertEqual(task2.make_filter(
            type='person', occupation='was here'), expected_filter)

    def test_make_filter_missing_key(self):
        with self.assertRaises(KeyError):
            task2.make_filter(name='Bill', age=30)

    def test_make_filter_wrong_value_type(self):
        with self.assertRaises(TypeError):
            task2.make_filter(type='person', occupation=100)


class TestFilter(unittest.TestCase):

    def test_filter_apply(self):
        filtered_data = task2.Filter([
            lambda item: item['name'] == 'polly',
            lambda item: item['type'] == 'bird'
        ]).apply(task2.sample_data)
        self.assertEqual(filtered_data, [
            {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
        ])

    def test_filter_apply_no_result(self):
        filtered_data = task2.Filter([
            lambda item: item['name'] == 'John',
            lambda item: item['type'] == 'person'
        ]).apply(task2.sample_data)
        self.assertEqual(filtered_data, [])


if __name__ == '__main__':
    unittest.main()
