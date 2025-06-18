#encapsulation in python
class Vehicle:
    #public function
    def displayName():
        return "Ford"
    
    #protected function
    def _displaymodel():
        return "Mustang"
    
    #private function
    def __engine():
        return "V8"
    
    #public function to display prv and protected data
    def displayDetails():
        name = Vehicle.displayName()
        model = Vehicle._displaymodel()
        engine = Vehicle.__engine()
        return f"Name: {name}, Model: {model}, Engine: {engine}"
    
vehicle = Vehicle()
    
print(Vehicle.displayName())
print(Vehicle._displaymodel())
print(Vehicle.displayDetails())