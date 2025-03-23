class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b

if __name__ == '__main__':
    calc = Calculator()
    print('Addition:', calc.add(1, 2))
    print('Subtraction:', calc.subtract(5, 3))
    print('Multiplication:', calc.multiply(4, 2))
    print('Division:', calc.divide(8, 4))import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        with self.assertRaises(ValueError):
            self.calc.divide(8, 0)

if __name__ == '__main__':
    unittest.main()