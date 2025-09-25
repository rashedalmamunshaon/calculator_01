# tests/test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide, mod


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (2.5, 0.5, 3.0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_mod():
    assert mod(10, 3) == 1


def test_mod_by_zero():
    with pytest.raises(ValueError):
        mod(1, 0)
