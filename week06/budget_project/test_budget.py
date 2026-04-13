# test_budget.py

from budget import calculate_savings, calculate_savings_rate


def test_calculate_savings():
    assert calculate_savings(5000, 2000) == 3000
    assert calculate_savings(1000, 1000) == 0


def test_calculate_savings_rate():
    assert calculate_savings_rate(5000, 2000) == 60
    assert calculate_savings_rate(1000, 500) == 50
    assert calculate_savings_rate(0, 500) == 0