# Cóbhan Phillipson 2018-05-28

def factorial(i):
     number = 1
     while i >= 1:
         number = number * i
         i = i - 1
     return number

print("The factorial of number 5 is:",factorial(5))
print("The factorial of number 7 is:",factorial(7))
print("The factorial of number 10 is:",factorial(10))