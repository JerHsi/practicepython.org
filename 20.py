def bSearch(L, num):
  start_index = 0
  end_index = len(L)-1
  #mid_index = len(L)//2
  
  
  while end_index - start_index != 0:
    if num < L[start_index] or num > L[end_index]:
      return False
    
    mid_index = (end_index - start_index) //2
    print(mid_index)
    
    if L[mid_index] == num:
      return True
      #break
    elif L[mid_index] > num:
      end_index = mid_index
    elif L[mid_index] < num:
      start_index = mid_index+1
