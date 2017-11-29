import random

w = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
num = "1234567890"
c = "!@#$%^&*()_+"
combo = w + num + c
  
def passGen():
  n = int(input("How many characters"))
  #print(random.choice(combo))
  password = ''
  for _ in range(n):
    password += random.choice(combo)
  return password

def passGen2():
  n = int(input("How many characters"))
  password = "".join(random.sample(combo,n))
  return password
