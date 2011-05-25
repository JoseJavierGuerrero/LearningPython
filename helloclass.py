class Vehicle():
	
    """store info of a vehicle"""


    def __init__ (self, brand, numTires=4):
        self.brand = brand
        self.tires = numTires
    
    def print_vehicle(self):
        print "Brand =" + str(self.brand) 
        print "Tires =" + str(self.tires)
        print
    
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
    anyCar.print_vehicle()
    aFord = Car("Ford")
    aFord.print_vehicle()
    aYamaha = MotorBike("Yamaha")
    aYamaha.print_vehicle()