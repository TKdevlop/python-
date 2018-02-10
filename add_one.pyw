def s(array):
    result=[None]
    n=len(array)
    carry=1
    for i in range(n-1,0):
            sums=array[i]+carry
            if sums==10:
                carry=1
            else:
                carry=0
            result[i]=sums%10
    return result        


print(s([1,2,3]))

            
            
            
            
            
