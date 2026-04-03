"""
File: receipt.py
Author: Stanley Adeyemi Eberendu
Description: A robust grocery POS (Point of Sale) system that processes 
customer requests against an inventory database to generate a detailed receipt.

--- (Enhancements) ---
1. BOGO (Buy One Get One) Discount: Implemented a 50% discount on every second unit of '1 cup yogurt' (ID: D083) purchased.
2. Coupon Generation: Logic added to print a 10% discount coupon for 
the most expensive item in the customer's current order.
3. Formatting: Used tabulate-style alignment for a professional receipt look.
"""

import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """
    Reads a CSV file and transforms it into a compound dictionary.
    Performance: O(n) where n is the number of products.
    """
    compound_dict = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                compound_dict[key] = row
    return compound_dict

def main():
    # Configuration Constants
    PRODUCT_FILE = "products.csv"
    REQUEST_FILE = "request.csv"
    TAX_RATE = 0.06
    DISCOUNTED_PRODUCT_ID = "D083" # 1 cup yogurt

    # Column Indexes
    ID_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QTY_INDEX = 1

    try:
        # 1. Initialize Data
        products_dict = read_dictionary(PRODUCT_FILE, ID_INDEX)

        # 2. Receipt Header
        print("-" * 30)
        print("    INKOM EMPORIUM FRESH MARKET    ")
        print("-" * 30)
        print()

        subtotal = 0
        total_items = 0
        highest_price = 0
        coupon_item = ""

        # 3. Process Request File
        with open(REQUEST_FILE, "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            print("Items:")
            for row in reader:
                prod_id = row[ID_INDEX]
                quantity = int(row[QTY_INDEX])

                # Data Lookup (Triggers KeyError if ID is invalid)
                product_data = products_dict[prod_id]
                name = product_data[NAME_INDEX]
                price = float(product_data[PRICE_INDEX])

                # Enhancement: Buy One Get One Half Off (D083)
                if prod_id == DISCOUNTED_PRODUCT_ID and quantity >= 2:
                    half_off_units = quantity // 2
                    full_price_units = quantity - half_off_units
                    item_total = (full_price_units * price) + (half_off_units * price * 0.5)
                    print(f"{name}: {quantity} @ {price} (BOGO 50% Applied)")
                else:
                    item_total = quantity * price
                    print(f"{name}: {quantity} @ {price}")

                # Tracking for Totals and Coupon
                total_items += quantity
                subtotal += item_total
                
                if price > highest_price:
                    highest_price = price
                    coupon_item = name

        # 4. Final Calculations
        sales_tax = subtotal * TAX_RATE
        total_due = subtotal + sales_tax

        # 5. Output Footer
        print()
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total_due:.2f}")
        print()
        print("Thank you for choosing Inkom Emporium Fresh Market!")

        # Timestamp in specified format: Wed Nov 4 05:10:30 2020
        now = datetime.now()
        print(f"{now:%a %b %d %H:%M:%S %Y}")

        # Enhancement: Targeted Coupon
        if coupon_item:
            print("\n*** VALUED CUSTOMER COUPON ***")
            print(f"Take 10% OFF your next {coupon_item}!")
            print("-" * 30)

    except FileNotFoundError:
        print(f"Error: The file '{PRODUCT_FILE}' or '{REQUEST_FILE}' was not found.")
        print("Please ensure the data files are in the same directory as the script.")
    except KeyError as e:
        print("Error: Unknown Product ID detected in order.")
        print(f"Product ID: {e}")
    except PermissionError:
        print("Error: Permission denied. Please close the CSV files if they are open in Excel.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()