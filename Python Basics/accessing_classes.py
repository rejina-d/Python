#importing classes and functions

from encapsulation import vehicle

class Car(Vehicle):
    def displayCarDetails():
        print("Car details:")
        
car = Car
car.displayCarDetails()  # Output: Car details:
print(car.displayDetails())
