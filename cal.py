import tkinter as tk
from sympy import symbols, sympify, solve, sin, cos, tan, log, ln, sqrt, exp, Abs, factor, expand

# Define symbolic variables
x, y = symbols('x y')

# Create main window
root = tk.Tk()
root.title("Advanced Calculator")

# Input field
equation_entry = tk.Entry(root, font=('Arial', 18), width=30, bd=5, relief='ridge')
equation_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Output label
solution_label = tk.Label(root, text="", font=('Arial', 16), fg='blue')
solution_label.grid(row=1, column=0, columnspan=5)

# Button click handler
def on_click(value):
    equation_entry.insert(tk.END, value)

# Clear input/output
def clear():
    equation_entry.delete(0, tk.END)
    solution_label.config(text="")

# Evaluate expression
def evaluate():
    expr = equation_entry.get().replace("abs", "Abs")
    try:
        result = sympify(expr)
        solution_label.config(text=f"Result: {result}")
    except Exception:
        solution_label.config(text="Error")

# Solve expression for x
def solve_expr():
    expr = equation_entry.get()
    try:
        result = solve(sympify(expr), x)
        solution_label.config(text=f"Solution: {result}")
    except Exception:
        solution_label.config(text="Error solving")

# Button layout
buttons = [
    ['7', '8', '9', '+', 'sin'],
    ['4', '5', '6', '-', 'cos'],
    ['1', '2', '3', '*', 'tan'],
    ['0', '(', ')', '/', 'log'],
    ['sqrt', 'exp', 'abs', 'ln', 'simplify'],
    ['factor', 'expand', 'C', '=', 'solve']
]

# Create buttons dynamically
for i, row in enumerate(buttons):
    for j, label in enumerate(row):
        if label == 'C':
            cmd = clear
        elif label == '=':
            cmd = evaluate
        elif label == 'solve':
            cmd = solve_expr
        else:
            cmd = lambda val=label: on_click(val)

        tk.Button(root, text=label, width=6, height=2, font=('Arial', 14),
                  command=cmd, bg="powder blue").grid(row=i+2, column=j, padx=5, pady=5)

# Run the app
root.mainloop()