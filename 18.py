import random

r = str(random.randint(1000,9999))
print(r)
bulls = -1
cows = 0

while cows != 4:
  cows = 0
  guess = input("Guess a 4 digit number: ")
  for i in range(0,4):
    if guess[i] == r[i]:
      cows += 1
  bulls += 1
  print("cows: " + str(cows) + ', bulls: ' + str(bulls))
