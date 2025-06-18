#functions in python
#always in camel case
def displayHelloWorld():
    print("Hello, World")
    
#function with no arg and return value
def add ():
    num1 = 10
    num2 = 20
    sum = num1 +num2
    return sum


#function with arg and no return value
def displayName(name):
    print("Hello, "+ name + "!w")
    
    
#function with arg and return value
def displayData(num1, num2):
    prod = num1 +num2
    return prod

displayHelloWorld() #calling the function
result = add() +10 #calling the function and storing the resukt in a variable
print(result) #printing the result

your_name = "Jhon"
displayName("your_name")

def fidplayData (num1, num2):
    prod = num1  * num2
    return prod
print(displayData(50,20))   
    
