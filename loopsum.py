# Cóbhan Phillipson, 2018-04-28
# Sum of all the even numbers from 1-100

sum = 0
i = 0

while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print("The sum of the numbers from 1 to 100:", sum)