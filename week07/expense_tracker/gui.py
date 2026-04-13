# gui.py

import tkinter as tk
from tracker import calculate_balance, categorize_expense, save_expense


def calculate():
    try:
        income = float(txt_income.get())
        expense = float(txt_expense.get())

        balance = calculate_balance(income, expense)
        category = categorize_expense(expense)

        lbl_result.config(
            text=f"Balance: {balance:.2f} | Category: {category}"
        )

        save_expense(income, expense)
        lbl_status.config(text="Saved successfully")

    except ValueError:
        lbl_status.config(text="Invalid input")


def clear():
    txt_income.delete(0, tk.END)
    txt_expense.delete(0, tk.END)
    lbl_result.config(text="")
    lbl_status.config(text="")


# GUI
root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Income").grid(row=0, column=0)
txt_income = tk.Entry(root)
txt_income.grid(row=0, column=1)

tk.Label(root, text="Expense").grid(row=1, column=0)
txt_expense = tk.Entry(root)
txt_expense.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=2, column=0)
tk.Button(root, text="Clear", command=clear).grid(row=2, column=1)

lbl_result = tk.Label(root, text="")
lbl_result.grid(row=3, column=0, columnspan=2)

lbl_status = tk.Label(root, text="", fg="red")
lbl_status.grid(row=4, column=0, columnspan=2)

root.mainloop()