class Car():
    def __init__(self, brand):
        self.brand = brand

    def get_brand(self):
        print(self.brand)

    def open_door(self, door_number):
        if door_number == 1:
            print("Opening  Driver's door")
        elif door_number == 2:
            print("Opening  Copilot's door")
        elif door_number == 3:
            print("Opening  Passenger's driver side door")
        elif door_number == 4:
            print("Opening  Passenger's copilots side door")
        elif door_number == 5:
            print("Opening trunk")
        elif door_number == 6:
            print("Opening Front hood")
        else:
            print("Sorry this door does not exist on this car")

    def blinker_control(self,left_blinker, right_blinker=None):
         if left_blinker == "On":
             self.left_blinker = left_blinker
             self.right_blinker = "Off"
         elif right_blinker == "On":
             self.left_blinker = "Off"
             self.right_blinker = right_blinker
         print("L : "+str(self.left_blinker)+ " - R: "+str(self.right_blinker))
