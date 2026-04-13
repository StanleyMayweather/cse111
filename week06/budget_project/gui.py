# gui.py

import tkinter as tk
from budget import calculate_savings, calculate_savings_rate


def on_calculate():
    """Handles calculate button click."""

    try:
        income = float(txt_income.get())
        expenses = float(txt_expenses.get())

        savings = calculate_savings(income, expenses)
        rate = calculate_savings_rate(income, expenses)

        lbl_result.config(
            text=f"Savings: {savings:.2f} | Rate: {rate:.2f}%"
        )

        lbl_status.config(text="")  # clear status

    except ValueError:
        lbl_status.config(text="Error: Please enter valid numbers")


def clear_fields():
    """Clears all inputs and outputs."""
    txt_income.delete(0, tk.END)
    txt_expenses.delete(0, tk.END)
    lbl_result.config(text="")
    lbl_status.config(text="")


# ---------------- GUI SETUP ---------------- #

root = tk.Tk()
root.title("Budget Calculator")

# Income
tk.Label(root, text="Income:").grid(row=0, column=0)
txt_income = tk.Entry(root)
txt_income.grid(row=0, column=1)

# Expenses
tk.Label(root, text="Expenses:").grid(row=1, column=0)
txt_expenses = tk.Entry(root)
txt_expenses.grid(row=1, column=1)

# Buttons
btn_calc = tk.Button(root, text="Calculate", command=on_calculate)
btn_calc.grid(row=2, column=0)

btn_clear = tk.Button(root, text="Clear", command=clear_fields)
btn_clear.grid(row=2, column=1)

# Result
lbl_result = tk.Label(root, text="")
lbl_result.grid(row=3, column=0, columnspan=2)

# Status bar
lbl_status = tk.Label(root, text="", fg="red")
lbl_status.grid(row=4, column=0, columnspan=2)

root.mainloop()