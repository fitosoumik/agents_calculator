```python
def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+,-,*,/): ")
            num2 = float(input("Enter second number: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:
                print("Invalid operation")
                continue

            print(f"Result: {result}")

            if input("Calculate again? (y/n): ").lower() != 'y':
                break

        except ValueError:
            print("Please enter valid numbers")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except:
            print("An error occurred")

if __name__ == "__main__":
    calculator()
```