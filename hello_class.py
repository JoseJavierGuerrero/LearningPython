class Vehicle():
    
    """store info of a vehicle"""


    def __init__ (self, brand, numTires=4):
        self.brand = brand
        self.tires = numTires
    
    def __str__(self):
        return '\n'.join(["Brand = " + str(self.brand), 
                          "Tires = " + str(self.tires)]) + '\n'
    
class Car(Vehicle):

    """store info of a car"""

    
    def __init__(self, brand=None):
        Vehicle.__init__(self,brand)

class MotorBike(Vehicle):

    """store info of a motorbike"""
    

    def __init__(self, brand=None):
        Vehicle.__init__(self,brand,2)


if __name__ == "__main__":
    anyCar = Car()
    print anyCar.__str__()
    aFord = Car("Ford")
    print aFord
    aYamaha = MotorBike("Yamaha")
    print str(aYamaha)