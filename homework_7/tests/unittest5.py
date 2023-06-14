import unittest
from code.hw5 import KeyValueStorage


class TestKeyValueStorage(unittest.TestCase):
    def test_string_values(self):
        storage = KeyValueStorage('test_data_string.txt')
        self.assertEqual(storage['name'], 'John')
        self.assertEqual(storage.last_name, 'Doe')
        self.assertEqual(storage.song_name, 'Bohemian Rhapsody')

    def test_integer_values(self):
        storage = KeyValueStorage('test_data_integer.txt')
        self.assertEqual(storage.age, 25)
        self.assertEqual(storage.weight, 80)
        self.assertEqual(storage.height, 180)

    def test_mixed_values(self):
        storage = KeyValueStorage('test_data_mixed.txt')
        self.assertEqual(storage.first_value, 42)
        self.assertEqual(storage.second_value, 'hello')
        self.assertEqual(storage.third_value, 3.14)

    def test_attribute_clash(self):
        with self.assertRaises(ValueError):
            storage = KeyValueStorage('test_data_clash.txt')

    def test_incorrect_value(self):
        with self.assertRaises(ValueError):
            storage = KeyValueStorage('test_data_incorrect.txt')


if __name__ == '__main__':
    unittest.main()
