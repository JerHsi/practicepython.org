import random

while True:
  choice = int(input("Enter a number:\n 1) Rock\n 2) Paper \n 3) Scissors\n"))
  
  #0 is rock
  #1 is paper
  #2 is scissors
  rps = ["rock", "paper", "scissors"]
  
  comp = random.randint(0,2)
  
  print("You choose: ", rps[choice-1])
  print("Computer choose: #", comp+1, " ",rps[comp])
  
  #if (rock and rock) or (paper and paper) or (scissors and scissors):
  if (choice-1) == comp:
    print("You both tie!")
  #elif (rock and paper) or (paper and scissors) or (scissors and rock):
  elif(choice-1 == 0 and comp == 1) or (choice-1 == 1 and comp == 2) or (choice-1 == 2 and comp == 0):
    print("You loose!")
  #elif (rock and scissors) or (scissors and paper) or (paper and rock):
  elif(choice-1 == 0 and comp == 2) or (choice-1 == 2 and comp == 1) or (choice-1 == 1 and comp == 0):
    print("You win!")
  
  usr_command = input("Enter your command: (Type \"quit\" to quit or any other key to continue playing.")
  if usr_command == "quit":
    break
  

