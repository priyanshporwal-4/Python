#Assignment 1


# 1. Write a program to print your name.
print("Genie")

# 2. Write a program to swap 2 numbers using a 3rd variable.
num1 = 10
num2 = 20
temp = num1
num1 = num2
num2 = temp
print(num1, num2)

# 3. Write a program to swap 2 numbers without using a 3rd variable.
num1 = 10
num2 = 20
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(num1, num2)

# 4. Write a program to swap 3 numbers using a 4th variable.
num1 = 10
num2 = 20
num3 = 30
temp = num1
num1 = num2
num2 = num3
num3 = temp
print(num1, num2, num3)

# 5. Write a program to swap 3 numbers without using a 4th variable.
num1 = 10
num2 = 20
num3 = 30
num1 = num1 + num2 + num3
num2 = num1 - (num2 + num3)
num3 = num1 - (num2 + num3)
num1 = num1 - (num2 + num3)
print(num1, num2, num3)

# 6. WAP to calculate the area and circumference of a circle.
import math

radius = 5

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("Area:", area)
print("Circumference:", circumference)

# 7. WAP to calculate the area and perimeter of a rectangle.
length = 10
width = 5

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)

# 8. Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary.
basic_salary = float(input("Enter the basic salary: "))

dearness_allowance = 0.4 * basic_salary
house_rent_allowance = 0.2 * basic_salary

gross_salary = basic_salary + dearness_allowance + house_rent_allowance

print("Gross Salary:", gross_salary)

# 9. Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program to convert this temperature into Centigrade degrees.
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

centigrade = (fahrenheit - 32) * 5 / 9

print("Temperature in Centigrade:", centigrade)

# 10. Temperature of a city in Centigrade degrees is input through the keyboard. Write a program to convert this temperature into Fahrenheit degrees.
centigrade = float(input("Enter temperature in Centigrade: "))

fahrenheit = (centigrade * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# 11. Write a program to calculate the average of 5 numbers input by the user.
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))

average = (num1 + num2 + num3 + num4 + num5) / 5

print("Average:", average)

# 12. Write a program to take a character and display its ASCII value.
char = input("Enter a character: ")

ascii_value = ord(char)

print("ASCII value:", ascii_value)

# 13. Write a program for the below formulas: (a+b)^2, (a+b)^3, (a-b)^2, (a-b)^3
a = 5
b = 3

result1 = (a + b) ** 2
result2 = (a + b) ** 3
result3 = (a - b) ** 2
result4 = (a - b) ** 3

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
print("Result 4:", result4)

# 14. The distance between 2 cities is input through the keyboard, WAP to convert & print this distance in meter, feet, inches & centimeter.
distance = float(input("Enter distance between two cities in kilometers: "))

meter = distance * 1000
feet = distance * 3280.84
inches = distance * 39370.1
centimeter = distance * 100000

print("Distance in Meter:", meter)
print("Distance in Feet:", feet)
print("Distance in Inches:", inches)
print("Distance in Centimeter:", centimeter)

# 15. WAP that takes a character in upper case and print it in lower case.
char = input("Enter a uppercase character: ")

lowercase_char = char.lower()

print("Lowercase char:", lowercase_char)

# 16. WAP that takes a character in lower case and print it in upper case.
char = input("Enter a lowercase character: ")

uppercase_char = char.upper()

print("Uppercase char:", uppercase_char)

# 17. Write a program to implement Heron's formula.
a = 5
b = 6
c = 7

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("Area:", area)

# 18. Enter the four-digit number through the Keyboard? WAP to find the sum of its all digits.
num = int(input("Enter a four-digit number: "))

thousands_digit = num // 1000
hundreds_digit = (num % 1000) // 100
tens_digit = (num % 100) // 10
units_digit = num % 10

sum_of_digits = thousands_digit + hundreds_digit + tens_digit + units_digit

print("Sum of digits:", sum_of_digits)


#Assignment 2


# 1. Write a program to print "Python is fun".
print("Python is fun")

# 2. Write a program to define variables in python and print the type of variables.
variable1 = 10
variable2 = "Hello"
variable3 = 3.14

print(type(variable1))
print(type(variable2))
print(type(variable3))

# 3. Today is a holiday at the children's camp, so all the children will be served ice cream.
# There are 68 children in the group and each child should get 2 scoops of ice cream.
# Your Task is, Write a program to calculate and output the total number of ice cream scoops we need.
total_children = 68
scoops_per_child = 2

total_scoops_needed = total_children * scoops_per_child
print("Total number of ice cream scoops needed:", total_scoops_needed)

# 4. Calculate and output the number of miles in 1000 kilometers using floor division operator.
# Hint : One mile is 1.6 kilometers, so find the quotient of 1000 and 1.6.
kilometers = 1000
miles = kilometers // 1.6
print("Number of miles in 1000 kilometers:", miles)

# 5. What is the output of following operation: print(1 + 4*3)
print(1 + 4*3) # Output: 13

# 6. What is the output of following operation: print(3**2//2)
print(3**2//2) # Output: 4

# 7. Let's use exponentiation to solve a known problem.
# You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days (the resulting amount is doubled every day).
# Task: Write a program to calculate the amount that will result from the doubling to understand which choice results in a larger amount.
amount_1 = 1000000
amount_2 = 0.01
days = 30

total_amount_1 = amount_1
total_amount_2 = amount_2

for day in range(days):
    total_amount_2 *= 2

print("Total amount with $1,000,000:", total_amount_1)
print("Total amount with penny doubled every day:", total_amount_2)

# 8. Write a program to create calculator and perform addition, subtraction, multiplication, division and remainder with two integer numbers.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
remainder = number1 % number2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Remainder:", remainder)

# 9. Write a program to interchange first and last elements in a list.
my_list = [1, 2, 3, 4, 5]
first_element = my_list[0]
last_element = my_list[-1]

my_list[0] = last_element
my_list[-1] = first_element

print("Interchanged list:", my_list)

# 10. Write a program to swap two elements in a list.
my_list = [1, 2, 3, 4, 5]
index1 = 1
index2 = 3

temp = my_list[index1]
my_list[index1] = my_list[index2]
my_list[index2] = temp

print("Swapped list:", my_list)

# 11. Write a program to calculate the average of 5 numbers given by the user.
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))
number4 = float(input("Enter fourth number: "))
number5 = float(input("Enter fifth number: "))

average = (number1 + number2 + number3 + number4 + number5) / 5
print("Average:", average)

# 12. Write a program to calculate the sum of each digit in a number (Input number by user.)
number = int(input("Enter a number: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print("Sum of digits:", sum_of_digits)

# 13. Write a Python program which accepts the radius of a circle from the user and compute the area.
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius**2
print("Area of the circle:", area)

# 14. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = last_name + " " + first_name
print("Reversed Name:", full_name)

# 15. Write a Python program to display the first and last colors from the following list:
color_list = ["Red", "Green", "White", "Black"]
first_color = color_list[0]
last_color = color_list[-1]

print("First color:", first_color)
print("Last color:", last_color)


#Assignment 3


# 1. Write a Python program to sum all the items in a list.
def sum_items(lst):
    return sum(lst)

# 2. Write a Python program to multiply all the items in a list.
def multiply_items(lst):
    result = 1
    for item in lst:
        result *= item
    return result

# 3. Write a Python program to get the largest number from a list.
def get_largest(lst):
    return max(lst)

# 4. Write a Python program to get the smallest number from a list.
def get_smallest(lst):
    return min(lst)

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
def count_strings(lst):
    count = 0
    for string in lst:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# 6. Write a Python program to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))

# 7. Write a Python program to check a list is empty or not.
def is_list_empty(lst):
    return len(lst) == 0

# 8. Write a Python program to clone or copy a list.
def copy_list(lst):
    return lst.copy()

# 9. Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that prints out all the elements of the list that are less than 5.
def print_elements_less_than_5(lst):
    for num in lst:
        if num < 5:
            print(num)

# 10. Take two lists, say for example these two: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
def get_common_elements(a, b):
    return list(set(a) & set(b))

# 11. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
even_numbers = [num for num in a if num % 2 == 0]

# 12. Write one line of Python that takes this list a and makes a new list that has only the odd elements of this list in it.
odd_numbers = [num for num in a if num % 2 != 0]

# 13. Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
new_list = [a[0], a[-1]]

# 14. Write a program to reverse a list.
reversed_list = lst[::-1]

# 15. Write a program to turn every item of a list into its square.
squared_list = [item ** 2 for item in lst]

# 16. Write a program to add new item to list after a specified item.
def add_item_after(lst, specified_item, new_item):
    index = lst.index(specified_item)
    lst.insert(index + 1, new_item)

# 17. Write a program to Extend nested list by adding the sublist.
def extend_nested_list(nested_lst, sublist):
    nested_lst.extend(sublist)

# 18. Write a program to replace a list's item with a new value if found.
def replace_item(lst, current_item, new_item):
    if current_item in lst:
        index = lst.index(current_item)
        lst[index] = new_item



#Assignment 4


# 1. Program to find out if input number is divisible by 2, 3, 5, 7, and 9 or not
def check_divisibility(number):
    if number % 2 == 0:
        print("Number is divisible by 2")
    if number % 3 == 0:
        print("Number is divisible by 3")
    if number % 5 == 0:
        print("Number is divisible by 5")
    if number % 7 == 0:
        print("Number is divisible by 7")
    if number % 9 == 0:
        print("Number is divisible by 9")

# 2. Program to find out the maximum number between two numbers
def find_maximum(a, b):
    if a > b:
        print(f"{a} is the maximum number")
    else:
        print(f"{b} is the maximum number")

# 3. Program to find out the maximum number between three numbers
def find_maximum_three(a, b, c):
    if a >= b and a >= c:
        print(f"{a} is the maximum number")
    elif b >= a and b >= c:
        print(f"{b} is the maximum number")
    else:
        print(f"{c} is the maximum number")

# 4. Program to find out the minimum number between two numbers
def find_minimum(a, b):
    if a < b:
        print(f"{a} is the minimum number")
    else:
        print(f"{b} is the minimum number")

# 5. Program to find out the minimum number between three numbers
def find_minimum_three(a, b, c):
    if a <= b and a <= c:
        print(f"{a} is the minimum number")
    elif b <= a and b <= c:
        print(f"{b} is the minimum number")
    else:
        print(f"{c} is the minimum number")

# 6. Program to check if two numbers are equal or not
def check_equality(a, b):
    if a == b:
        print("The numbers are equal")
    else:
        print("The numbers are not equal")

# 7. Program to determine whether a year is leap year or not
def check_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Leap year")
    else:
        print("Not a leap year")

# 8. Program to determine whether a year is a leap year or not using conditional operator
def check_leap_year_conditional(year):
    leap = "Leap year" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "Not a leap year"
    print(leap)

# 9. Program to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

# 10. Program to calculate total expenses with discount
def calculate_expenses(quantity, price_per_item):
    if quantity > 1000:
        discount = 0.1 * quantity * price_per_item
        total_expenses = quantity * price_per_item - discount
    else:
        total_expenses = quantity * price_per_item
    
    print(f"Total expenses: {total_expenses}")

# 11. Program to give bonus based on years of service
def give_bonus(current_year, joined_year):
    if current_year - joined_year > 3:
        print("Bonus of Rs. 2500/- given")
    else:
        print("No bonus")

# 12. Program to calculate gross salary based on basic salary
def calculate_gross_salary(basic_salary):
    if basic_salary < 1500:
        HRA = 0.1 * basic_salary
        DA = 0.9 * basic_salary
    else:
        HRA = 500
        DA = 0.98 * basic_salary
    
    gross_salary = basic_salary + HRA + DA
    print(f"Gross Salary: {gross_salary}")

# 13. Program to determine the type of character entered
def check_character_type(character):
    if character.isalpha():
        if character.isupper():
            print("Capital letter")
        else:
            print("Small case letter")
    elif character.isdigit():
        print("Digit")
    else:
        print("Special symbol")

# 14. Program to determine division based on subject marks
def calculate_division(marks):
    percentage = sum(marks) / len(marks)
    
    if percentage >= 60:
        division = "First Division"
    elif 50 <= percentage <= 59:
        division = "Second Division"
    elif 40 <= percentage <= 49:
        division = "Third Division"
    else:
        division = "Fail"
    
    print(f"Division: {division}")

# 15. Program to check if a number is positive, negative or zero
def check_number(number):
    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")

# 16. Program to determine if a driver is insured or not based on marital status, gender and age
def check_insurance(marital_status, gender, age):
    if marital_status == "married" or (gender == "male" and age > 30) or (gender == "female" and age > 25):
        print("Driver is insured")
    else:
        print("Driver is not insured")

# 17. Program to check if a triangle is valid based on its angles
def check_triangle(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 == 180:
        print("Triangle is valid")
    else:
        print("Triangle is not valid")

# 18. Program to check if a character is a small case alphabet or special symbol
def check_character_type_conditional(character):
    result = "Small case alphabet" if character.islower() else "Special symbol"
    print(result)


#Assignment 5



# 1. Write python script to print value of the key.
my_dict = {"key": "value"}
print(my_dict["key"])

# 2. Write a python script to print all keys of dictionary.
print(my_dict.keys())

# 3. Write a python script to find the sum of all items in the dictionary.
sum_of_items = sum(my_dict.values())
print(sum_of_items)

# 4. Write a python script to check if a key exists in a dictionary or not.
key_to_check = "key"
if key_to_check in my_dict:
    print("Key exists")
else:
    print("Key does not exist")

# 5. Write a python script to check if a value exists in a dictionary or not.
value_to_check = "value"
if value_to_check in my_dict.values():
    print("Value exists")
else:
    print("Value does not exist")

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 5
generated_dict = {x: x*x for x in range(1, n+1)}
print(generated_dict)

# 7. Write a Python program to remove a key from a dictionary.
key_to_remove = "key"
my_dict.pop(key_to_remove)
print(my_dict)

# 8. Write a Python program to get the maximum and minimum value in a dictionary.
max_value = max(my_dict.values())
min_value = min(my_dict.values())
print("Max Value:", max_value)
print("Min Value:", min_value)



#Assignment 6



# 1. Count Number of Lowercase Characters in a String
def count_lowercase(string):
    count = 0
    for char in string:
        if char.islower():
            count += 1
    return count

# 2. Check if a String is a Palindrome or Not
def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

# 3. Count Upper Case alphabets, Lower Case alphabets,
# digit and special symbol in a given string/statement
def count_characters(string):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1
    return uppercase_count, lowercase_count, digit_count, special_count

# 4. Convert upper case letter into lower case letter
def convert_to_lower(string):
    return string.lower()

# 5. Convert lower case letter into upper case letter
def convert_to_upper(string):
    return string.upper()

# 6. Find length of a string given by the user using predefined function
# and also by your own logic
def get_length(string):
    # Using predefined function
    length = len(string)

    # By own logic
    count = 0
    for char in string:
        count += 1
    return length, count

# 7. Copy one string into another string given by the user
# using pre-defined function and also by your own logic
def copy_string(string):
    # Using predefined function
    copied_string = string.copy()

    # By own logic
    copied_string = ""
    for char in string:
        copied_string += char
    return copied_string

# 8. Concatenate one string with another string given by the user
# using predefined function and also by your own logic
def concatenate_strings(string1, string2):
    # Using predefined function
    concatenated_string = string1 + string2

    # By own logic
    concatenated_string = ""
    for char in string1:
        concatenated_string += char
    for char in string2:
        concatenated_string += char
    return concatenated_string

# 9. Compare one string with another string given by the user
# using predefined function and also by your own logic
def compare_strings(string1, string2):
    # Using predefined function
    if string1 == string2:
        return True
    else:
        return False

    # By own logic
    if len(string1) != len(string2):
        return False
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False
    return True

# 10. Reverse the string given by user and print the reverse string
# using predefined function and also by your own logic
def reverse_string(string):
    # Using predefined function
    reversed_string = string[::-1]

    # By own logic
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string
