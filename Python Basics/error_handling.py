#error handling in python

try:
    result = 5/0
    print(result)
    
except ZeroDivisionError as e:
    print(e)
    
    
    
try:
    result = 15/0
    print(result)
    

except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed")
    
    
try:
    num = int(input("Enter a number: "))
    print(num)
    
except (ValueError, TypeError) as e:
    print(e)
    

try:
    num1 = int(input("Enter an odd number:"))
    if num1 % 2 == 0:
        raise ValueError("Error: Number is even")
    else:
        print(num1)
except ValueError as e:
    print(e)
    
else:
    print("No exception occurred")
    
finally:
    print("Final block executed")
    