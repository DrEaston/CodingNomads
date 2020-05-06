'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''
import unittest

def double_square(n):
    return n*n*2

class TestMath(unittest.TestCase):
    def test_square_then_double(self):
        self.assertEqual(double_square(3), 18)
    def test_even(self):
        self.assertEqual(double_square(3)%2, 0)
    def test_odd(self):
        self.assertEqual(double_square(3)%2, 1)


unittest.main()