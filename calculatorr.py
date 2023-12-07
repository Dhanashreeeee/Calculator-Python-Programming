import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        result_var.set("Invalid input")
        return

    operation = operation_var.get()

    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result_var.set("Error: Division by zero")
            return
    else:
        result_var.set("Invalid operation")
        return

    result_var.set(f"Result: {result}")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widgets
entry_num1 = ttk.Entry(root, width=15, font=('Helvetica', 16))
entry_num2 = ttk.Entry(root, width=15, font=('Helvetica', 16))

# Dropdown for operations
operation_var = tk.StringVar()
operation_var.set("Add")
operation_dropdown = ttk.Combobox(root, textvariable=operation_var, values=["Add", "Subtract", "Multiply", "Divide"], font=('Helvetica', 16))

# Result display
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, font=('Helvetica', 16))

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate, style='TButton', width=15)

# Configure style for the button
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 16))

# Layout using grid
entry_num1.grid(row=0, column=0, padx=10, pady=10)
operation_dropdown.grid(row=0, column=1, padx=10, pady=10)
entry_num2.grid(row=0, column=2, padx=10, pady=10)
calculate_button.grid(row=1, column=0, columnspan=3, pady=10)
result_label.grid(row=2, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
