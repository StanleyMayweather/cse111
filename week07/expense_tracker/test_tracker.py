# test_tracker.py

from tracker import calculate_balance, categorize_expense


def test_calculate_balance():
    assert calculate_balance(5000, 2000) == 3000
    assert calculate_balance(1000, 1000) == 0


def test_categorize_expense():
    assert categorize_expense(30) == "Low"
    assert categorize_expense(150) == "Medium"
    assert categorize_expense(300) == "High"