import vehicles.car

myCar = vehicles.car.Car("Ford")
myCar.get_brand()
print("\nDoor of your car:\n"
       "1 - Driver's door\n"
       "2 - Copilot's door\n"
       "3 - Passenger's driver side door\n"
       "4 - Passenger's copilots side door\n"
       "5 - Trunk\n"
       "6 - Front hood\n")

door_number = int(input("Enter the door number: "))

myCar.open_door(door_number)

myCar.blinker_control(right_blinker="OM")