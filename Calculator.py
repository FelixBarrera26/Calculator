import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to append the clicked button's value to the entry widget
def append_to_expression(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + str(value))

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget to display the expression and results
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
for i in range(9):
    button = tk.Button(window, text=str(i + 1), padx=10, pady=5, command=lambda num=i + 1: append_to_expression(num))
    button.grid(row=(i // 3) + 1, column=i % 3)

# Create the operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, padx=10, pady=5, command=lambda op=operator: append_to_expression(op))
    button.grid(row=i + 1, column=3)

# Create the equals button
equals_button = tk.Button(window, text='=', padx=10, pady=5, command=evaluate_expression)
equals_button.grid(row=4, column=2)

# Create the clear button
clear_button = tk.Button(window, text='C', padx=10, pady=5, command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=4, column=0)

# Run the main loop
window.mainloop()