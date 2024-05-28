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
root.geometry("400x400")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

category_label = ttk.Label(main_frame, text="Category:")
category_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

category_entry = ttk.Entry(main_frame)
category_entry.grid(row=0, column=1, padx=10, pady=5)

amount_label = ttk.Label(main_frame, text="Amount:")
amount_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

amount_entry = ttk.Entry(main_frame)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

add_button = ttk.Button(main_frame, text="Add Expense", command=add_expense)
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.EW)

delete_button = ttk.Button(main_frame, text="Delete Expense", command=delete_expense)
delete_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.EW)

listbox = tk.Listbox(main_frame)
listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.NSEW)

scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.grid(row=4, column=2, sticky=tk.NS)
listbox.config(yscrollcommand=scrollbar.set)

update_expenses()

root.mainloop()
