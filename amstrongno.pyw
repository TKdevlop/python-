n=int(153)
temp= n
sums= 0
while(n>0):
      r=n%10
      n=n/10
      sums= sums+ r*r*r
    
if(temp==sums):
    print("its an armstrong no")
    
else:
    print("hell no")
    print(sums)
    print(n)
