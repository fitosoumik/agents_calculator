class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError('Cannot divide by zero')
        return x / y

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(1, 2))
    print(calc.subtract(5, 3))
    print(calc.multiply(4, 2))
    print(calc.divide(10, 2))