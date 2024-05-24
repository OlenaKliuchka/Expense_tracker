import tkinter as tk
from tkinter import ttk

expenses = {}

def add_expense():
    category = category_entry.get()
    amount = float(amount_entry.get())
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    update_expenses()

def delete_expense():
    category = category_entry.get()
    if category in expenses:
        del expenses[category]
    update_expenses()

def update_expenses():
    listbox.delete(0, tk.END)
    for category, amount in expenses.items():
        listbox.insert(tk.END, f"{category}: {amount}")

root = tk.Tk()
root.title("Expense Tracker")

style = ttk.Style()
style.configure("TButton", padding=10, font=("Arial", 12))
style.configure("TEntry", padding=10, font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))

category_label = ttk.Label(root, text="Category:")
category_label.pack()

category_entry = ttk.Entry(root)
category_entry.pack()

amount_label = ttk.Label(root, text="Amount:")
amount_label.pack()

amount_entry = ttk.Entry(root)
amount_entry.pack()

add_button = ttk.Button(root, text="Add Expense", command=add_expense)
add_button.pack()

delete_button = ttk.Button(root, text="Delete Expense", command=delete_expense)
delete_button.pack()

listbox = tk.Listbox(root)
listbox.pack()

update_expenses()

root.mainloop()
