#!/usr/bin/env python
# encoding: utf-8


class Vehicle(dict):
	
    """Store info of a vehicle"""

    def stripnulls(data): 
        "Strip whitespace and nulls" 
        return data.replace("\00", "").strip()

    __DATA_FORMAT = { "brand"    : (0,15,stripnulls),
                      "tires"    : (15,17,int),
                      "gasoline" : (17,20,int),
                      "km"       : (20,24,int) }


    def __init__ (self, brand, numTires=4):
        self.brand = brand
        self.tires = numTires
        self.gasoline = 50
        self.km = 0

    def __str__(self):
        return '\n'.join([	"Brand = " + str(self.brand), 
                          	"Tires = " + str(self.tires),
							"Gasoline = " + str(self.gasoline),
							"Kilometers = " + str(self.km)]) + '\n'

    def start(self):
        if self.gasoline != 0:
            print "The engine sounds..."
        else:
            print "You're out of gas :("
            
    def drive(self, gas):
        if self.gasoline < gas:
            self.gasoline -= gas
            self.km += gas
            print "The road slides under your car..."
        else:
            print "Not enough gas"
            
    def set_brand(self, brand_):
        self.brand = brand_

    def set_tires(self, tires_):
        self.tires = tires_

    def set_gasoline(self, gasoline_):
        self.gasoline = gasoline_

    def set_km(self, km_):
        self.km = km_
    
    def save_to_file(self, file_):
        f = open(file_, 'w')
        f.write(self.brand.ljust(15))
        f.write(str(self.tires).ljust(2))
        f.write(str(self.gasoline).ljust(3))
        f.write(str(self.km).ljust(4))

    def read_from_file(self, file_):
        f = open(file_, 'r')
        values = f.read()
        for attr_ , (start, end, parse_function) in self.__DATA_FORMAT.items():
            getattr(self, 'set_%s' % attr_)(parse_function(values[start:end]))
    

class Car(Vehicle):
	
    """Store info of a car"""

    def __init__(self, brand=None):
        Vehicle.__init__(self,brand)


class MotorBike(Vehicle):
	
    """Store info of a motorbike"""

    def __init__(self, brand=None):
        Vehicle.__init__(self,brand,2)


if __name__ == "__main__":
    any_car = Car()
    print any_car.__str__()
    a_ford = Car("Ford")
    print a_ford
    a_yamaha = MotorBike("Yamaha")
    print str(a_yamaha)