Temperature = input("Enter what you want to convert, write 'C' for Celcius and 'F' for Farheniet ")
print()
if Temperature=="C" :
    f = int(input("Enter temperature in Farheniet "))
    c = (f-32)*5/9
    print("Your converted value in Celcius is = ",c,"Celcius")
elif Temperature=="F" :
    c = int(input("Enter temperature in Celcius "))
    f = (c*9/5)+32
    print("Your converted value in Celcius is = ",f,"Farheniet")
else :
    print("Wrong input")
