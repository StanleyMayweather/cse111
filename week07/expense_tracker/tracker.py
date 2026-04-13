# tracker.py

import csv

FILE_NAME = "expenses.csv"


def calculate_balance(income, expenses):
    return income - expenses


def categorize_expense(amount):
    if amount < 50:
        return "Low"
    elif amount < 200:
        return "Medium"
    else:
        return "High"


def save_expense(income, expense):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([income, expense])


def read_expenses():
    data = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data