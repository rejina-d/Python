#calculator using python

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def __call__(self, operation):
        num1 = self.num1
        num2 = self.num2
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            return num1 / num2
        else:
            return "Invalid operation"
        
calc = Calculator(10,20)
result = (calc("add"))
print(result)  # Output: 30
print(calc("Test"))       
        
