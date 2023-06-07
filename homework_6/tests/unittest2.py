import unittest
from hw2 import backspace_compare


class TestBackspaceCompare(unittest.TestCase):

    def test_equal_strings(self):
        self.assertEqual(backspace_compare('abc', 'abc'), True)

    def test_single_backspace(self):
        self.assertEqual(backspace_compare('abc#', 'abc'), True)

    def test_backspace_at_beginning(self):
        self.assertEqual(backspace_compare('#abc', 'abc'), True)

    def test_one_string_empty(self):
        self.assertEqual(backspace_compare('abc#de', 'abde'), False)

    def test_multiple_backspaces(self):
        self.assertEqual(backspace_compare('a#bc#d###', 'a#c'), True)

    def test_empty_strings(self):
        self.assertEqual(backspace_compare('', ''), True)

    def test_only_backspaces(self):
        self.assertEqual(backspace_compare('#######', ''), True)


if __name__ == '__main__':
    unittest.main()