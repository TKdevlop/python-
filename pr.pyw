n=int(input("Enter a number"))
r=0
t=n
for i in range(1,n):
     if n%i==0:
         r=r+i
         
if t==r:
    print("perfect")
    print(i,n,r)
else:
    print("not perfect")
    print(i,n,r)
