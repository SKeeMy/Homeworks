import unittest
import importlib.util

spec = importlib.util.spec_from_file_location(
    "task_name", "C:\\Users\\SKeeMy\\Desktop\\Python\\tasks\homework_3\\code\\task1.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestCacheDecorator(unittest.TestCase):
    def test_cache_decorator_returns_value_from_function_first_time(self):
        @module.cache(times=2)
        def add(a, b):
            return a+b
        result1, is_cached1 = add(2, 3)
        self.assertEqual(result1, 5)
        self.assertFalse(is_cached1)

    def test_cache_decorator_returns_cached_value_second_time(self):
        @module.cache(times=2)
        def add(a, b):
            return a+b
        add(2, 3)
        result2, is_cached2 = add(2, 3)
        self.assertEqual(result2, 5)
        self.assertTrue(is_cached2)

    def test_cache_decorator_raises_typeerror_if_times_arg_is_not_int(self):
        with self.assertRaises(TypeError):
            @module.cache(times="2")
            def add(a, b):
                return a+b


def test_cache_decorator_raises_valueerror_if_times_arg_is_negative(self):
    with self.assertRaises(ValueError) as context:
        @module.cache(times=-1)
        def add(a, b):
            return a+b
    exception = context.exception
    self.assertIsInstance(exception, ValueError)
    self.assertEqual(
        str(exception), "Times argument must be a positive integer")


if __name__ == '__main__':
    unittest.main()
