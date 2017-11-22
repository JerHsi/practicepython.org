import random

count = 1
correct = 0
num_q = 5
math = ['+', '-']

while count <= num_q:
  a,b = random.randint(0,20), random.randint(0,10)
  operation = random.choice(math)
  
  if operation == '+':
    ans = int(input("\nQuestion #" + str(count) + ":\n " + str(a) + " + " + str(b) + " = "))
    if ans == a + b:
      correct += 1
  elif operation == '-':
    ans = int(input("\nQuestion #" + str(count) + ":\n " + str(a) + " - " + str(b) + " = "))
    if ans == a - b:
      correct += 1
    
  count +=1

#Grading system
perc = 100*correct/num_q
if perc == 100.0:
  grade = 'A+'
elif perc >= 90.0 and perc < 100.0:
  grade = 'A'
elif perc >= 80.0 and perc < 90.0:
  grade = 'B'
elif perc >= 70.0 and perc < 80.0:
  grade = 'C'  
elif perc >= 60.0 and perc < 70.0:
  grade = 'D'  
elif perc >= 50.0 and perc < 60.0:
  grade = 'E'  
else:
  grade = 'F'

print("\n\n" + "=" * 50 + "\nYou got " + str(correct) + " correct answers out of " + str(count-1) + " questions. \n\nYour grade is " + grade + "!!!!")










