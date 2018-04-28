# Cóbhan Phillipson 2018-04-01
# Guessing game

# Adapted from https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
from random import randint

target = randint(1, 100)
guess = 4

while guess != target: 
  guess = int(input("Please enter a guess between 1-100: "))
  if guess == target:
      print("Well done kid! You nailed it")
  elif guess < target:
      print("Too low!")
  else:
      print("too high!")
