import tkinter as tk

# Function to update the expression in the text entry
def update_expression(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + symbol)

# Function to evaluate the expression and display the result
def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("520x960")  # Adjusted size for the border

# Add a frame to act as the border with a thick border line
border_frame = tk.Frame(root, bg="white", bd=0.5, highlightthickness=1, highlightbackground="black", highlightcolor="black")
border_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

# Add another frame inside the border for the calculator layout
calc_frame = tk.Frame(border_frame, bg="black")
calc_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# Entry widget for displaying the expression and result
entry = tk.Entry(calc_frame, width=18, font=("Arial", 24), borderwidth=5, relief="sunken", justify='right', bg="lightgrey")
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=20)

# Custom button colors and styles
button_color = "#E06C75"  # Soft red buttons
button_text_color = "#FFFFFF"  # White text
operation_color = "#C678DD"  # Purple color for operations
equal_color = "#56B6C2"  # Cyan equals button

# Buttons layout for numbers and operations (added % operator)
buttons = [
    ('MC', 1, 0, "#333333"), ('M+', 1, 1, "#333333"), ('%', 1, 2, operation_color), ('/', 1, 3, operation_color),
    ('7', 2, 0, button_color), ('8', 2, 1, button_color), ('9', 2, 2, button_color), ('*', 2, 3, operation_color),
    ('4', 3, 0, button_color), ('5', 3, 1, button_color), ('6', 3, 2, button_color), ('-', 3, 3, operation_color),
    ('1', 4, 0, button_color), ('2', 4, 1, button_color), ('3', 4, 2, button_color), ('+', 4, 3, operation_color),
    ('0', 5, 0, button_color), ('.', 5, 2, button_color)
]

# Add buttons to the window
for (text, row, col, color) in buttons:
    if text == '=':
        tk.Button(calc_frame, text=text, width=5, height=2, font=("Arial", 20), 
                  bg=color, fg=button_text_color, command=evaluate_expression).grid(row=row, column=col, padx=10, pady=10)
    else:
        tk.Button(calc_frame, text=text, width=5, height=2, font=("Arial", 20), 
                  bg=color, fg=button_text_color, 
                  command=lambda t=text: update_expression(t)).grid(row=row, column=col, padx=10, pady=10)

# Add the Clear button
tk.Button(calc_frame, text="C", width=5, height=2, font=("Arial", 20), 
          bg="#D19A66", fg=button_text_color, 
          command=clear_entry).grid(row=5, column=1, padx=10, pady=10)

# Add the Equals button
tk.Button(calc_frame, text="=", width=5, height=2, font=("Arial", 20), 
          bg=equal_color, fg=button_text_color, command=evaluate_expression).grid(row=5, column=3, padx=10, pady=10)

# Run the application
root.mainloop()
