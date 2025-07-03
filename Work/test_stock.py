"""Unittest
# Common self.assert Methods:
self.assertEqual(a, b): Checks if a == b.
self.assertNotEqual(a, b): Checks if a != b.
self.assertTrue(x): Checks if bool(x) is True.
self.assertFalse(x): Checks if bool(x) is False.
self.assertIs(a, b): Checks if a is b.
self.assertIsNot(a, b): Checks if a is not b.
self.assertIsNone(x): Checks if x is None.
self.assertIsNotNone(x): Checks if x is not None.
self.assertIn(a, b): Checks if a in b.
self.assertNotIn(a, b): Checks if a not in b.
self.assertIsInstance(a, b): Checks if isinstance(a, b).
self.assertNotIsInstance(a, b): Checks if not isinstance(a,b).
self.assertRaises(exception, callable, *args, **kwargs): Checks if a specific exception is raised 
    when callable is called with the given arguments.
"""


import stock
import unittest


class TestStock(unittest.TestCase):
    def test_create(self):
        "Test with a valid stock symbol"
        my_stock = stock.Stock("AAPL", 100, 150.0)
        self.assertEqual(my_stock.name, "AAPL")
        self.assertEqual(my_stock.shares, 100)
        self.assertEqual(my_stock.price, 150.0)
        self.assertEqual(my_stock.cost, 15000.0)

    def test_sell(self):
        "Test selling shares"
        my_stock = stock.Stock("AAPL", 100, 150.0)
        self.assertEqual(my_stock.sell(50), 50)

    def test_attribute_error(self):
        """Test with an invalid stock symbol"""
        with self.assertRaises(AttributeError):
            # This line is incorrect; 'cost' is not a method of the module, but of the Stock class.
            stock.cost('INVALID')

    def test_over_sell(self):
        stockx = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            stockx.sell(1000) == 100


if __name__ == '__main__':
    unittest.main()
