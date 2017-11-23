a = [5, 10, 15, 20, 25]

def slice(s):
  return s[:1] + s[-1:] if len(a) > 1 else s
print(slice(a))
