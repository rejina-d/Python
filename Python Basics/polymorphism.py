# Polymorphism in Python

class A:
    def displayName(self):
        print("Class A's display name")
        
    def displayHello(self):
        print("Hello")
        
class B(A):
    def displayName(self):
        print("Class B's display name")
        
class C(B):
    def displayName(self):
        print("Class C's display name")
        
    def add(self, *args):
        sum = 0
        for num in args:
            sum += num
        return sum

# Create object instances (not classes!)
obj = A()
obj.displayName()  # Output: Class A's display name

obj1 = B()
obj1.displayName()  # Output: Class B's display name

obj3 = C()
obj3.displayName()  # Output: Class C's display name
obj3.displayHello()  # Output: Hello

# Using add method with *args
result = obj3.add(10)
print(result)  # Output: 10

result1 = obj3.add(10, 20, 30)
print(result1)  # Output: 60

result2 = obj3.add(10, 20, 30, 40, 50)
print(result2)  # Output: 150
