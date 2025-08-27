import unittest
from calculator import Calculator

class TestIntegration(unittest.TestCase):

    def test_workflow(self):
        calc = Calculator()
        sum_val = calc.add(10, 20)
        product = calc.multiply(sum_val, 2)
        self.assertEqual(product, 60)

if __name__ == "__main__":
    unittest.main()
