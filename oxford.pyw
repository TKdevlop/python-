def recur(n):
    if n<=1:
        return n
    else:
        return recur(n-1) + recur(n-2)

print(recur(4))    


##def fab(n):
##    a=0
##    b=1
##    for i in range(1,n):
##        c=a+b
##        a=b 
##        b=c
##    return c
##
##
##print(fab(40))        
def lis(a):
    
