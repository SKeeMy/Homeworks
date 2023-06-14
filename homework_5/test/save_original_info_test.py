import unittest
from code.save_original_info import preserve_info, print_result


class TestPreserveInfo(unittest.TestCase):

    def test_docstring(self):
        @preserve_info
        def foo():
            """test"""
            return 42
        self.assertEqual(foo.__doc__, 'test')

    def test_name(self):
        @preserve_info
        def bar():
            return 42
        self.assertEqual(bar.__name__, 'bar')

    def test_original_func(self):
        @preserve_info
        def foo():
            return 42
        self.assertIs(foo.__original_func, foo)

    def test_print_result(self):
        def my_print(*args, **kwargs):
            pass

        @print_result(printer=my_print)
        def foo():
            return 42
        self.assertEqual(foo(), None)

    def test_custom_sum(self):
        self.assertEqual(custom_sum.__doc__,
                         'This function can sum any objects which have __add___')
        self.assertEqual(custom_sum.__name__, 'custom_sum')
        self.assertIs(custom_sum.__original_func, custom_sum)


if __name__ == '__main__':
    unittest.main()
