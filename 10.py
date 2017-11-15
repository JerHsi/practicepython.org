import random

def createList(num, l):
  for i in range(num):
    l.append(random.randint(1,100))

num_a = random.randint(1,100)
num_b = random.randint(1,100)
a,b,c = [],[],[]

'''
for i in range(num_a):
  a.append(random.randint(1,100))

for i in range(num_b):
  b.append(random.randint(1,100))
'''
createList(num_a, a)
createList(num_b, b)
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in range(len(a)):
  if a[i] in b and a[i] not in c:
    c.append(a[i])
print(sorted(c))
