"""
Sentinel Budget Manager
Author: Stanley Adeyemi Eberendu
Description: A tool to track and analyze personal finances.
"""

import csv
import os

def main():
    """Main entry point for the Sentinel Budget Manager."""
    print("--- Sentinel Budget Manager ---")
    
    filename = "expenses.csv"
    
    try:
        # 1. Load Data
        transactions = load_transactions(filename)
        
        # 2. Logic: Aggregate Data
        category_totals = calculate_category_totals(transactions)
        
        # 3. Output results
        print("\nSpending Summary:")
        for category, amount in category_totals.items():
            print(f"{category}: ${amount:.2f}")
            
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found. Starting with a blank slate.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def load_transactions(filename):
    """
    Reads transactions from a CSV file.
    Returns: A list of transaction dictionaries.
    """
    transactions = []
    with open(filename, "rt") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions

def calculate_category_totals(transactions):
    """
    Logic Function (Testable): Sums amounts by category.
    Parameters: transactions (list of dicts)
    Returns: dictionary {category: total_amount}
    """
    totals = {}
    for item in transactions:
        cat = item.get("category", "Other")
        # Ensure we convert the string amount to a float safely
        try:
            amount = float(item.get("amount", 0))
        except ValueError:
            amount = 0
            
        if cat in totals:
            totals[cat] += amount
        else:
            totals[cat] = amount
    return totals

def validate_currency(value):
    """
    Logic Function (Testable): Validates that a string can be a 
    positive float representing money.
    """
    try:
        val = float(value)
        if val < 0:
            return False
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    main()