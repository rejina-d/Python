#Arthmetic operator
#1. Addition +
#2. Subtraction -
#3. Multiplication *
#4. Division /
#5. Modulus %
#6. Exponentiation **
#7. Floor Division //

num1 =10
num2 = 15

# Addition
sum = num1 + num2
print("Sum of two numbers is:", sum)

#Modulus
rem = num2 % num1
print(rem)

#Exponential
pow = num1 ** num2
print(pow)

#Division
div = num2/2
print(div)


#####
#Comparision operator:
#1. Equal to ==
#2. Not Equal to !=
#3. Greater than >
#4. Less than <
#5. Greater than or equal to >=
#6. Less than or equal to <=

print (num1>num2)
print (num1!=num2)
print (num1==num2)
print (num1>=num2)

#Logical operators: (multiple condition check garna)
#1. AND (and)   
#2. OR (or)
#3. NOT (not)

#and (euta true vayesi sabai true)
print(num1>=num2 and num2<=num1)
print(num2>=num1 and num1<=num2)

#or
print(num1>=num2 or num2<=num1)
print(num2>=num1 or num1<=num2)
print (not num1>num2)

#Assignment operator
#1. = (assign)
#2. += (add and assign)
#3. -= (subtract and assign)
#4. *= (multiply and assign)
#5. /= (divide and assign)
#6. %= (modulus and assign)
#7. **= (exponent and assign)

num1 = num1+1
print(num1)

num1+=1
print(num1)

num1 **= 2
print(num1)