import unittest
from code.hw2 import Order, morning_discount, elder_discount


class TestOrder(unittest.TestCase):
    def test_morning_discount(self):
        order = Order(100, morning_discount)
        self.assertEqual(order.final_price(), 75)

    def test_elder_discount(self):
        order = Order(100, elder_discount)
        self.assertEqual(order.final_price(), 50)

    def test_no_discount(self):
        order = Order(100)
        self.assertEqual(order.final_price(), 100)

    def test_invalid_discount_type(self):
        with self.assertRaises(TypeError):
            order = Order(100, 'string')


if __name__ == '__main__':
    unittest.main()
