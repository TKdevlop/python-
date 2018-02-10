low = 0
high = arrSize - 1 

while low <=  high:

  mid = (low + high) / 2

  if arr[mid] == key:         #// CHANGE
   if arr[mid] == key  and  mid == 0 or arr[mid-1] != key :
    return mid
  elif  key < arr[mid]: # // CHANGE
    elif  key <= arr[mid]: 
    high = mid - 1
  else
    low = mid + 1        

return -1
