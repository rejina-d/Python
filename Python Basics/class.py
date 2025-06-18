#class in python
class A:
    def displayClassA():
        print("This is Class A")
        
#inheritance in python
class B(A):
    def displayClassB():  
        print("This is class B")
        
class C(B):
    def displayClassC():  
        print("This is class C")
        
#creating an instance of class A
obj = A
#obj.displayClassA()
obj2 = B
#obj2.displayClassB() #output: This is class B
#obj2.displayClassA() #output: This is class A inherited by class B
obj3 = C
obj3.displayClassC() #output: This is class C
obj3.displayClassB() 
obj3.displayClassA()


