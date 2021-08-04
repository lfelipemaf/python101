name = input("What is your name? ")
print("Hello "+name)
print("Welcome to your first Python program")
print(" I hope you enjoy this new journey")

myInt = 3 #Integer number
print(type(myInt))
myFloat = 2.0 #Float number
print(type(myFloat))
myStr = "Hello" #String
print(type(myStr))
myList = [myInt, myFloat, myStr] #List of values
print(type(myList))
myTurple = (myList,myStr,myInt) #Turple is a lista that can not be changed
print(type(myTurple))
myDict = {"color": "red", "age": 28} #Dictionary
print(type(myDict))

#Operations
num1 = int(input("\nNum1: "))
print(type(num1))
num2 = int(input("\nNum2: "))
print(type(num2))
print(num1 + num2) #add
print(num1 - num2) #subtract
print(num1 * num2) #multiply
print(num1 / num2) #Divide
print(num1 ** num2) #power
print(num1 % num2) #remainder

print(myStr[1])
print(myStr[1:4])

print(myList)
myList.append(5)
print(myList)
myList.pop(1)
print(myList)