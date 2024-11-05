# gui.py
import tkinter as tk
from tkinter import messagebox

def union(set1, set2):
    return set1 | set2

def intersection(set1, set2):
    return set1 & set2

def difference(set1, set2):
    return set1 - set2

def symmetric_difference(set1, set2):
    return set1 ^ set2

def parse_set(input_str):
    try:
        return set(map(int, input_str.split(',')))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a comma-separated list of integers.")
        return None

def perform_operation(operation):
    set1 = parse_set(entry_set1.get())
    set2 = parse_set(entry_set2.get())
    if set1 is None or set2 is None:
        return

    if operation == 'union':
        result = union(set1, set2)
    elif operation == 'intersection':
        result = intersection(set1, set2)
    elif operation == 'difference':
        result = difference(set1, set2)
    elif operation == 'symmetric_difference':
        result = symmetric_difference(set1, set2)

    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Set Calculator")

tk.Label(root, text="Set 1 (comma-separated):").grid(row=0, column=0, padx=10, pady=10)
entry_set1 = tk.Entry(root)
entry_set1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Set 2 (comma-separated):").grid(row=1, column=0, padx=10, pady=10)
entry_set2 = tk.Entry(root)
entry_set2.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Union", command=lambda: perform_operation('union')).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Intersection", command=lambda: perform_operation('intersection')).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Difference", command=lambda: perform_operation('difference')).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Symmetric Difference", command=lambda: perform_operation('symmetric_difference')).grid(row=3, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()