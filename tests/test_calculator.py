"""Тесты для калькулятора."""
import pytest
from src.calculator import add, subtract, multiply, divide

def test_add():
    """Тест сложения."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -3) == -8

def test_subtract():
    """Тест вычитания."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-2, -4) == 2

def test_multiply():
    """Тест умножения."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0

def test_divide():
    """Тест деления."""
    assert divide(6, 2) == 3
    assert divide(10, 4) == 2.5
    assert divide(-8, 2) == -4

def test_divide_by_zero():
    """Тест деления на ноль."""
    with pytest.raises(ValueError, match="Нельзя делить на ноль!"):
        divide(5, 0)