def fibo():
  N = int(input("How many numbers?"))
  i = 1
  fib = []
  fib.append(1)
  fib.append(1)
  
  if N == 1:
    print(fib[0])
  elif N == 2:
    print(sum(fib))
  else:
    while i < N-1:
      fib.append(fib[i-1] + fib[i])
      i+=1
    print(sum(fib))
