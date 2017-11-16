N = int(input())

if all(N%i for i in range(2,N)) or N==1:
  print("it's prime")
else:
  print("Not prime")
