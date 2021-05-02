from abc import ABC,abstractmethod
class AbstractDemo(ABC):        #ABSTRACT CLASS
    @abstractmethod
    def HouseInterest(self):     #abstract method
        None
    @abstractmethod
    def VehicalInterest(self):
        None

class SBI(AbstractDemo):                #CONCRETE CLASS
    def HouseInterest(self):
        print("house interest 9%")
    def VehicalInterest(self):
        print("vehical interest 8%")

sbiobj=SBI()
sbiobj.VehicalInterest()
