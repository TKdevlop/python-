phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char=="A" or char=="a":
    print ("X"),
  else:
    print (char),
  
def digit_sum(n):
  new=0
  while(n>0):
    r=n%10
    n=n//10
    new=new+r
  return new
    
    
print(digit_sum(500))    
  
  
  
