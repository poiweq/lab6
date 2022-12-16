import pytest
from postfix_calculator import PostfixCalculator


def test_1():
    assert PostfixCalculator.compute("1 4 + 48 12 - *") == 180


def test_2():
    assert PostfixCalculator.compute("74 12 + 53 12 - * 151 /") == 23


def test_3():
    assert PostfixCalculator.compute("123 12 / 123 * 4221 -") == -2991
