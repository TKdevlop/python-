def median(array): 
  
  n=len(array)
  array=sorted(array)
  lis=array
  if n%2==0:
      mid=n//2
      middle=(mid+mid-1)//2
      return (lis[middle]+lis[mid])/2
  else:
      mid=0+n//2
      return lis[mid]
     
    

print(median([4, 5, 5, 4]))
