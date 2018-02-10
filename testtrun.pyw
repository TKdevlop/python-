def selection():
    A=[9,8,7,6,5,4,3,2]
    n=len(A)
    for i in range(0,n-1):
        imin=i
        for j in range(i+1,n):
            if(A[j]<A[imin]):
               imin=j
        temp=A[i]
        A[i]=A[imin]
        A[imin]=temp
        
        
print(selection())

               
               
               
