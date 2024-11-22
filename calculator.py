import tkinter as tk
from tkinter import messagebox
from itertools import chain, combinations

def union(set1, set2):
    result = set1.copy()
    for item in set2:
        if item not in result:
            result.add(item)
    return result

def intersection(set1, set2):
    result = {item for item in set1 if item in set2}
    return result

def difference(set1, set2):
    result = {item for item in set1 if item not in set2}
    return result

def symmetric_difference(set1, set2):
    result = {item for item in set1 if item not in set2}
    result.update({item for item in set2 if item not in set1})
    return result

def is_subset(set1, set2):
    for item in set1:
        if item not in set2:
            return False
    return True

def is_superset(set1, set2):
    for item in set2:
        if item not in set1:
            return False
    return True

def is_disjoint(set1, set2):
    for item in set1:
        if item in set2:
            return False
    return True

def cardinality(set1):
    count = 0
    for _ in set1:
        count += 1
    return count

def power_set(s):
    s = list(s)
    result = []
    for r in range(len(s) + 1):
        result.extend(combinations(s, r))
    return result

def parse_set(input_str):
    try:
        elements = input_str.split(',')
        return set(elements)
    except Exception as e:
        messagebox.showerror("Invalid input", f"Error parsing input: {str(e)}")
        return None

def perform_operation_set1(operation):
    set1 = parse_set(entry_set1.get())
    if set1 is None:
        return

    if operation == 'cardinality':
        result = cardinality(set1)
    elif operation == 'power_set':
        result = power_set(set1)

    result_label.config(text=f"Result: {result}")

def perform_operation_set2(operation):
    set2 = parse_set(entry_set2.get())
    if set2 is None:
        return

    if operation == 'cardinality':
        result = cardinality(set2)
    elif operation == 'power_set':
        result = power_set(set2)

    result_label.config(text=f"Result: {result}")

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
    elif operation == 'is_subset':
        result = is_subset(set1, set2)
    elif operation == 'is_superset':
        result = is_superset(set1, set2)
    elif operation == 'is_disjoint':
        result = is_disjoint(set1, set2)

    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Set Calculator")
root.configure(bg='#77AA77')

tk.Label(root, text="Set 1 (comma-separated):", bg='#77AA77', fg='pink').grid(row=0, column=0, padx=10, pady=10)
entry_set1 = tk.Entry(root, bg='#77AA77')
entry_set1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Set 2 (comma-separated):", bg='#77AA77', fg='pink').grid(row=1, column=0, padx=10, pady=10)
entry_set2 = tk.Entry(root, bg='#77AA77')
entry_set2.grid(row=1, column=1, padx=10, pady=10)

button_style = { 'bg':'#77AA77', 'fg': 'pink', 'highlightthickness': 0, 'borderwidth': 0, 'highlightbackground': '#77AA77'}
tk.Button(root, text="Union", command=lambda: perform_operation('union'), **button_style).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Intersection", command=lambda: perform_operation('intersection'), **button_style).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Difference", command=lambda: perform_operation('difference'), **button_style).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Symmetric Difference", command=lambda: perform_operation('symmetric_difference'), **button_style).grid(row=3, column=1, padx=10, pady=10)
tk.Button(root, text="Is Subset", command=lambda: perform_operation('is_subset'), **button_style).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Is Superset", command=lambda: perform_operation('is_superset'), **button_style).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Cardinality Set 1", command=lambda: perform_operation_set1('cardinality'), **button_style).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Cardinality Set 2", command=lambda: perform_operation_set2('cardinality'), **button_style).grid(row=5, column=1, padx=10, pady=10)
tk.Button(root, text="Power Set Set 1", command=lambda: perform_operation_set1('power_set'), **button_style).grid(row=6, column=0, padx=10, pady=10)
tk.Button(root, text="Power Set Set 2", command=lambda: perform_operation_set2('power_set'), **button_style).grid(row=6, column=1, padx=10, pady=10)
tk.Button(root, text="Is Disjoint", command=lambda: perform_operation('is_disjoint'), **button_style).grid(row=7, column=0, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ", bg='#77AA77', fg='pink')
result_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()