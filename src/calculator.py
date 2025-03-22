Here's a simple calculator implemented in Python with a basic graphical user interface using tkinter:

```python
import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x400")

        # Create display
        self.display = tk.Entry(self.window, width=25, font=('Arial', 16), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Button labels
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        # Create and place buttons
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.window, text=button, width=5, height=2, command=cmd).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, key):
        if key == '=':
            # Calculate result
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == 'C':
            # Clear display
            self.display.delete(0, tk.END)
        else:
            # Add pressed key to display
            self.display.insert(tk.END, key)

    def run(self):
        self.window.mainloop()

# Create and run calculator
calc = Calculator()
calc.run()
```

This calculator includes:
1. Basic arithmetic operations (+, -, *, /)
2. Decimal point support
3. Clear function
4. Error handling for invalid expressions

Alternatively, here's a simpler console-based calculator:

```python
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Enter 'q' to quit")
    
    while True:
        # Get input from user
        num1 = input("Enter first number: ")
        if num1.lower() == 'q':
            break
            
        operation = input("Enter operation: ")
        if operation.lower() == 'q':
            break
            
        num2 = input("Enter second number: ")
        if num2.lower() == 'q':
            break
            
        # Convert string inputs to float
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
            
        # Perform calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero")
                continue
            result = num1 / num2
        else:
            print("Invalid operation")
            continue
            
        print(f"Result: {result}")
        print()

calculator()
```

This console-based calculator:
1. Takes two numbers and an operation as input
2. Supports basic arithmetic operations
3. Handles invalid inputs and division by zero
4. Allows the user to quit by entering 'q'
5. Continues running until the user chooses to quit

Choose either version based on your needs. The GUI version is more user-friendly but requires tkinter, while the console version is simpler but more basic in functionality.