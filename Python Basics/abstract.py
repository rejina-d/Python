#abstract in python

from abc import ABC

class Wallets(ABC):
    
    @abstractmethod
    def pay(self):
        pass

class Paypal(Wallets):
    def pay(self):
        print("Paypal payment successful")
        
    def displayName():
        print("Paypal")
        
class Khalti(Wallets):
    def pay(self):
        print("Khalti payment successful")
    
def payment(wallet: Wallets, amount):
    wallet.pay(amount)
    
wallet = input("Enter wallet name")
amount= float(input("Enter amount"))

if wallet == "Paypal":
    payment(Paypal(), amount)
elif wallet.lower() == "Khalti":
    payment(Khalti(), amount) 
else:
    print("Invalid wallet")
        
obj= Paypal
obj.pay()
obj.displayName()