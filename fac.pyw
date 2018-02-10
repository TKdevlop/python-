def palin(n):
    t=n
    rev=0
    while(n>0):
        i=n%10
        n=n//10
        rev=rev+i*i*i
        
    if t==rev:
        return "Its a palindrome number"
    else:
        return"it is not a palindrome number"


print(palin(123))    
        
        
