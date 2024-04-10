import unittest
import random

def add_two_numbers(a, b):
    return a + b

def multiply_three_numbers(a,b,c):
    return a * b * c


class Test_add_function(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_two_numbers(1, 2), 3)
    def test_add_negative_numbers(self):
        self.assertEqual(add_two_numbers(-1, -2), -3)
    def test_mixed_numbers(self):
        self.assertEqual(add_two_numbers(1, -2), -1)

    def test_two_positive_mult(self):
        self.assertEqual(multiply_three_numbers(2, 3, 4), 24)
    def test_two_negative_mult(self):
        self.assertEqual(multiply_three_numbers(-2, -4, 4), 32)


if __name__ == '__main__':
    a,b,c = int(random.randint(0,5)) , int(random.randint(0,5)), int(random.randint(0,5))
    print(f'sum of {a} and {b} is {add_two_numbers(a,b)}')
    print(f'multiplication of {a},{b} and {c} is { multiply_three_numbers(a,b,c)}')
    unittest.main()