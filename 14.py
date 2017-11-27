def removeDup(L):
  ans = []
  for i in L:
    if i not in ans:
      ans.append(i)
  return ans
  
def use_sets(L):
  return list(set(L))
