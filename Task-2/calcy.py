import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            result = "Invalid Operation"

        label_result.config(text=f"Result: {result:.2f}")
    except ValueError:
        label_result.config(text="Please enter valid numbers")
    except ZeroDivisionError:
        label_result.config(text="Error: Division by zero")

# Set up the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("1200x800")
root.resizable(True, True)
root.configure(bg="#2d2d2d")

# Set up custom styles
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14), background="#2d2d2d", foreground="white")
style.configure("TEntry", font=("Helvetica", 14))
style.configure("TButton", font=("Helvetica", 12), background="#5cb85c", foreground="white")
style.configure("TMenubutton", font=("Helvetica", 14))

# Header
header = ttk.Label(root, text="Simple Calculator", font=("Helvetica", 18, "bold"))
header.pack(pady=10)

# Set up the input fields and labels
label_num1 = ttk.Label(root, text="Enter first number:")
label_num1.pack(pady=5)

entry_num1 = ttk.Entry(root, width=20, justify="center")
entry_num1.pack(pady=5)

label_num2 = ttk.Label(root, text="Enter second number:")
label_num2.pack(pady=5)

entry_num2 = ttk.Entry(root, width=20, justify="center")
entry_num2.pack(pady=5)

label_operation = ttk.Label(root, text="Choose operation:")
label_operation.pack(pady=5)

operation_var = tk.StringVar(value="+")
operation_menu = ttk.OptionMenu(root, operation_var, "+", "+", "-", "*", "/")
operation_menu.pack(pady=5)

# Set up the calculate button
button_calculate = ttk.Button(root, text="Calculate", command=calculate, style="TButton")
button_calculate.pack(pady=20)

# Set up the result label
label_result = ttk.Label(root, text="Result: ", font=("Helvetica", 16, "bold"))
label_result.pack(pady=10)

# Start the application
root.mainloop()

