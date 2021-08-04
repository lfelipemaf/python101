class Car:
    def __init__(self, brand):
        #magic method to initialize de Object, basicaly everytime you create a new car, you must pass a brand.
        self.brand = brand
        #The keyword self its referencing to this object
    def get_brand(self):
        print(self.brand)

myCar = Car("Ford")
myCar.get_brand()

class Truck(Car):
    # inherantance Truck has all the methods of car but also its own methods.
    def tow_car(self):
        print("Towing a car")

myTruck = Truck("VW")
myTruck.get_brand()
myTruck.tow_car()