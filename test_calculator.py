import pytest
from calculator import add, subtract, multiply, divide


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, -3) == -5


def test_subtract_positive():
    assert subtract(10, 5) == 5


def test_subtract_negative():
    assert subtract(-5, -3) == -2


def test_multiply_positive():
    assert multiply(4, 3) == 12


def test_multiply_zero():
    assert multiply(5, 0) == 0


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)