import unittest
from code.hw1 import find_occurrences, example_tree


class TestFindOccurrences(unittest.TestCase):

    def test_int(self):
        self.assertEqual(find_occurrences(example_tree, 1), 0)

    def test_bool_true(self):
        self.assertEqual(find_occurrences(example_tree, True), 0)

    def test_bool_false(self):
        self.assertEqual(find_occurrences(example_tree, False), 0)

    def test_str_red(self):
        self.assertEqual(find_occurrences(example_tree, 'RED'), 4)

    def test_str_blue(self):
        self.assertEqual(find_occurrences(example_tree, 'BLUE'), 2)

    def test_non_existing_key(self):
        self.assertEqual(find_occurrences(example_tree, 'non_existing_key'), 0)

    def test_nested_dict_key(self):
        self.assertEqual(find_occurrences(example_tree, 'key2'), 1)

    def test_nested_dict_key_value(self):
        self.assertEqual(find_occurrences(example_tree, 'value1'), 1)

    def test_nested_set_val(self):
        self.assertEqual(find_occurrences(example_tree, 'a'), 1)

    def test_nested_in_tuple(self):
        self.assertEqual(find_occurrences(example_tree, 'qwe'), 0)


if __name__ == '__main__':
    unittest.main()
