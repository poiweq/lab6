import unittest
from postfix_calculator import PostfixCalculator


class PostfixCalculatorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(PostfixCalculator.compute("1 4 + 48 12 - *"), 180)

    def test2(self):
        self.assertEqual(PostfixCalculator.compute("74 12 + 53 12 - * 151 /"), 23)

    def test3(self):
        self.assertEqual(PostfixCalculator.compute("123 12 / 123 * 4221 -"), -2991)


if __name__ == '__main__':
    unittest.main()
