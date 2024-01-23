# import numpy as np


class Calculator:
    """
    A simple calculator class that performs addition, subtraction, multiplication, and division.
    """

    def addition(self, a, b):
        """
        Add two numbers together.

        Parameters:
        a (int or float): The first number
        b (int or float): The second number

        Returns:
        int or float: The sum of a and b
        """
        return a + b

    def subtraction(self, a, b):
        """
        Subtract one number from another.

        Parameters:
        a (int or float): The number from which to subtract
        b (int or float): The number to subtract

        Returns:
        int or float: The result of a - b
        """
        return a - b

    def multiplication(self, a, b):
        """
        Multiply two numbers together.

        Parameters:
        a (int or float): The first number
        b (int or float): The second number

        Returns:
        int or float: The product of a and b
        """
        return a * b

    def division(self, a, b):
        """
        Divide one number by another.

        Parameters:
        a (int or float): The dividend
        b (int or float): The divisor

        Returns:
        int or float: The quotient of a / b
        str: Error message if division by zero is attempted
        """
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed"

import unittest
from test2 import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        result = self.calc.addition(10, 5)
        self.assertEqual(result, 15)

    def test_subtraction(self):
        result = self.calc.subtraction(10, 5)
        self.assertEqual(result, 5)

    def test_multiplication(self):
        result = self.calc.multiplication(10, 5)
        self.assertEqual(result, 50)

    def test_division(self):
        result = self.calc.division(10, 5)
        self.assertEqual(result, 2)

    def test_division_by_zero(self):
        result = self.calc.division(10, 0)
        self.assertEqual(result, "Error: Division by zero is not allowed")

if __name__ == '__main__':
    unittest.main()
