import os
from pathlib import Path
import unittest
from code.hw1 import merge_sorted_files

class TestMergeSortedFiles(unittest.TestCase):
    
    def setUp(self):
        self.files = ['file1.txt', 'file2.txt']
        self.data_dir = os.path.join(os.getcwd(), 'data')
        self.expected_output = [1, 2, 3, 4, 5, 6]
    
    def test_merge_sorted_files(self):
        file_list = [os.path.join(self.data_dir, f) for f in self.files]
        result = list(merge_sorted_files(file_list))
        self.assertEqual(result, self.expected_output)

if __name__ == '__main__':
    unittest.main()