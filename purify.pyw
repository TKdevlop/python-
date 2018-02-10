def purify(numbers):
    lis=[]
    for i in numbers:
        if i%2==0:
            lis.append(i)
    return lis        
     
      
        
      
     
      


print(purify([1,2,3,4,5,6]))   




def product(array):
  number=1
  for i in array:
    number=number*i
  return number  
    
