import unittest
from code.counter import instances_counter
 
 
class TestInstancesCounter(unittest.TestCase):
    def setUp(self):
        @instances_counter
        class TestClass:
            pass
        self.TestClass = TestClass

    def test_created_instances(self):
        obj1, obj2, obj3 = self.TestClass(), self.TestClass(), self.TestClass()
        self.assertEqual(obj1.get_created_instances(), 3)

    def test_reset_instances_counter(self):
        obj1, obj2, obj3 = self.TestClass(), self.TestClass(), self.TestClass()
        self.assertEqual(obj1.reset_instances_counter(), 3)
        self.assertEqual(obj1.get_created_instances(), 0)


if __name__ == '__main__':
    unittest.main()