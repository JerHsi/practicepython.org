def bSearch(L, num):
  start_index = 0
  end_index = len(L)-1
  #mid_index = len(L)//2
  
  while end_index - start_index != 0:
    if num < L[start_index] or num > L[end_index]:
      return False
    
    mid_index = ((end_index + start_index) //2)
    print(mid_index)
    print(start_index)
    print(end_index)
    print("------")
    
    if L[mid_index] == num or L[start_index] == num or L[end_index] == num:
      return True
      #break
    elif num < L[mid_index]:
      end_index = mid_index - 1
    elif num > L[mid_index]:
      start_index = mid_index + 1
