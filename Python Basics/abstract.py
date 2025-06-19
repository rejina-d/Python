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
        
obj= Paypal
obj.pay()
obj.displayName()