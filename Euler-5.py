# Cóbhan Phillipson, 2018-05-05
# Project Euler Problem 5 https://projecteuler.net/problem=5
# help from http://legobreath.sdf.org/euler5py.html
check = 2520
# check is set to 2520 because we already know is is the smallest number
# that can be divided by each of the numbers # from 1 to 10 without any remainder.
# we can use this as our starting point

i = 11
# i is set to 11 because we already know the solution of 
# numbers between 1 to 10 (2520).

while (i != 20):
    i = i+1
    if (check % i != 0):
        check = check + 2520
        i = 1
print ("%d" % check)