import os
import tempfile
import shutil
import unittest
from code.hw3 import universal_file_counter

class TestUniversalFileCounter(unittest.TestCase):
    
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        
        self.file1 = os.path.join(self.tmp_dir, "file1.txt")
        with open(self.file1, "w") as f:
            f.write("This is a test file.\nLine 2.")
            
        self.file2 = os.path.join(self.tmp_dir, "file2.txt")
        with open(self.file2, "w") as f:
            f.write("File 2.\nLine 2.\nLine 3.")
        
    def tearDown(self):
        shutil.rmtree(self.tmp_dir)
        
    def test_universal_file_counter_without_tokenizer(self):
        result = universal_file_counter(Path(self.tmp_dir), "txt")
        self.assertEqual(result, 6)
        
    def test_universal_file_counter_with_tokenizer(self):
        tokenizer = str.split
        result = universal_file_counter(Path(self.tmp_dir), "txt", tokenizer)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()