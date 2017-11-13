import random

r = random.randint(1,9)
g = int(input("Guess a number: "))

while True:
  if g==r:
    print("You got it!")
    break
  elif g>r:
    print("guess lower")
    g = int(input("Guess again: "))
  elif g<r:
    print("guess higher")
    g = int(input("Guess again: "))
