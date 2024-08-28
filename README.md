# Calculator

This Python code creates a simple calculator application using the Tkinter library, which provides a graphical user interface (GUI). The calculator has buttons for numbers, basic arithmetic operations, and additional functionalities like clearing the entry and calculating the result. The calculator is designed with custom styles, including colors and borders. Here’s a detailed description of the code:

1. Importing the Tkinter library:
The code begins by importing the Tkinter library, which is used for creating the GUI components.

2. Defining Functions:
update_expression(symbol): This function updates the expression displayed in the entry widget by appending the symbol (numbers or operators) that the user clicks on.
evaluate_expression(): This function evaluates the mathematical expression entered in the entry widget. If the expression is valid, it displays the result; otherwise, it shows an "Error" message.
clear_entry(): This function clears the entry field, resetting it for a new calculation.

3. Creating the Main Window:
root = tk.Tk(): Initializes the main window for the application.
root.title("Calculator"): Sets the title of the window to "Calculator".
root.geometry("520x960"): Specifies the size of the window.

4. Adding Frames:
border_frame: This frame acts as a border around the calculator, with a black border line.
calc_frame: This frame is placed inside the border frame and contains all the calculator buttons and the entry widget.

5. Entry Widget:
entry: This widget is used to display the expression and the result. It has custom styles, such as font size, background color, and text alignment to the right.

6. Defining Button Layout:
The buttons are organized in a grid layout, with each button having specific properties like size, color, and command.
button_color, button_text_color, operation_color, equal_color: These variables define custom colors for the buttons, including soft red for numbers, purple for operations, and cyan for the equals button.

7. Adding Buttons:
The buttons are added to the calculator using a loop that iterates over a list of button properties (text, row, col, color).
The buttons are arranged in a grid layout with padding between them for a clean and organized look.

8. Clear and Equals Buttons:
Clear Button (C): Clears the current input when clicked.
Equals Button (=): Evaluates the expression and displays the result when clicked.

9. Running the Application:
root.mainloop(): This line starts the Tkinter event loop, making the application responsive and interactive.

10. Features:
Basic Arithmetic Operations: The calculator supports addition, subtraction, multiplication, division, and percentage operations.
Memory Buttons (MC, M+): Placeholder buttons for memory operations, though they currently do not have functionality attached.
Error Handling: The calculator handles errors by displaying "Error" in case of invalid expressions.

11. Styling and Appearance:
The calculator is styled with custom colors, padding, and borders to enhance its visual appeal and make it user-friendly. The layout is designed to be visually distinct, with separate sections for numbers and operations.
