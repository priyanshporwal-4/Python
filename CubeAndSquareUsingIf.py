import math
CubeOrSquare = input("Enter what you want to convert, write 'C' for Cube and 'S' for Square ")
a = int(input("Enter value of a "))
b = int(input("Enter value of b "))
print()
if CubeOrSquare =="C" :
    Cube = print(math.pow((a+b),3))
    print("Cube of numbers is ",Cube)
elif CubeOrSquare =="S" :
    Square = print(math.pow((a+b),2))
    print("Cube of numbers is ",Square)
else :
    print("Wrong Input")


    



