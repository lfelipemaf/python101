x = int(input("First number: "))
y =  int(input("Second number: "))

print("\n if statement \n")
if x < y:
    print( str(x) + " is lower then "+ str(y))
elif x > y:
    print(str(x) + " is bigger then " + str(y))
else:
    print(str(x) + " is equal to " + str(y))

list = [1,2,3,4,5]
print("\n for loop \n")
for val in list:
    print(val)

x = 0
print("\n while loop \n")
while x < 6:
    print(x)
    x+=1