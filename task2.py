import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values!")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

# Create widgets
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Label(root, text="Select operation:").pack(pady=5)
operation_var = tk.StringVar(value="Add")
operations_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
operations_menu.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Result:")
result_label.pack(pady=10)

# Run the application
root.mainloop()
