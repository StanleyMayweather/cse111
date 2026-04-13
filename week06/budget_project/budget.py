# budget.py

def calculate_savings(income, expenses):
    """Returns savings amount."""
    return income - expenses


def calculate_savings_rate(income, expenses):
    """Returns savings rate as a percentage."""
    if income == 0:
        return 0
    return (income - expenses) / income * 100