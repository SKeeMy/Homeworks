import unittest
from code.hw1 import SimplifiedEnum, ColorsEnum, SizesEnum


class TestSimplifiedEnum(unittest.TestCase):
    def test_colors_enum(self):
        self.assertEqual(ColorsEnum.RED, 'RED')
        self.assertEqual(ColorsEnum.BLUE, 'BLUE')
        self.assertEqual(ColorsEnum.ORANGE, 'ORANGE')
        self.assertEqual(ColorsEnum.BLACK, 'BLACK')

    def test_sizes_enum(self):
        self.assertEqual(SizesEnum.XL, 'XL')
        self.assertEqual(SizesEnum.L, 'L')
        self.assertEqual(SizesEnum.M, 'M')
        self.assertEqual(SizesEnum.S, 'S')
        self.assertEqual(SizesEnum.XS, 'XS')

    def test_keys_not_in_dict(self):
        with self.assertRaises(KeyError):
            ColorsEnum.WHITE

    def test_duplicate_keys(self):
        with self.assertRaises(TypeError):
            class TestEnum(metaclass=SimplifiedEnum):
                __keys = ("A", "B", "C", "B")


if __name__ == '__main__':
    unittest.main()
