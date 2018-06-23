# Cóbhan Phillipson, 2018-06-02

# Problem 1
def sumultiply(x, y):
    # Create a variable that will become the answer.
    total = 0
    # Loop over y, adding x to the total.
    for i in range(y):
        total = total + x
    return total
# Tests from question.
print(sumultiply(11, 13))
print(sumultiply(5, 123))

# Problem 2
def ispalindrome(s):
# Create a variable that will become the answer.
ans = True
# Loop over the length of the string
for i in range(len(s)):
    if s[i] != s[len(s) - i - 1]:
        ans = False
return ans

# Tests from question.
print(ispalindrome("radar"))
print(ispalindrome("radars"))

# Problem 3
def simpleinterest(p, r, n):
    # Calculate the interest for one period.
    i = p * (0.01 * r)
    # Calculate the interest for all periods.
    t = i * n
    # Return the total interest plus principal, rounded.
    return round(p + t, 2)

# Tests from question.
print(simpleinterest(1000, 3, 5))
print(simpleinterest(1000, 7, 10))

# Problem 4
def compoundinterest(p, r, n):
    # Loop over the periods.
    for i in range(n):
        # Increase the principal.
        p = p + (p * (0.01 * r))
    # Return the final principal, rounded to nearest cent.
    return round(p, 2)

# Tests from question.
print(compoundinterest(1000, 3, 5))
print(compoundinterest(1000, 7, 10))

# Problem 5
def newtonsroot(x):
    # Set the initial guess to anything. Try half of x.
    z = x / 2.0
    # Set the next guess using the formula.
    n = z - ((z**2 - x)/(2 * z))
    # Keep looping until the difference between the current guess
    # and the next guess is less than 0.000001.
    while abs(z - n) >= 0.0000001:
        z = n
        n = z - ((z**2 - x)/(2 * z))
    return n
    
# Tests from question.
print(newtonsroot(100))
print(newtonsroot(144))