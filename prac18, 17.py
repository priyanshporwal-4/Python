# char to ascii
print(ord(input("Enter a Character: ")[0]))

# four digits
i = input("Enter four digits: ")
sum = 0
for n in i:
    sum += int(n)
print(sum)

# heron's formula
a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))
c = int(input("Enter Value of c: "))
s = (a + b + c) / 2

inputNumber = s * ((s - a) * (s - b) * (s - c))

squareRoot = inputNumber ** (1 / 2)
print(f"\fArea of Triangle is : {squareRoot}")
