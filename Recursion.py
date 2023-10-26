# 1.
def factorial(n): 
    if n <= 1:
        return 1
    return factorial(n - 1) * n

# 2.
print(factorial(5))  

# 3.
def twoReturn():
    a, b=5, 6
    return a, b

print(twoReturn())

# break can only use inside loop






    