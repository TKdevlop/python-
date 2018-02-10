def binary(A,x,findfirst):
    
    count=0
    n=len(A)
    start=0
    end=n-1
    result=-1 # it means we have not found element in the array so far
   
    while(start<=end):
         mid=(start+end)//2
         if A[mid]==x:
             result= mid
             if findfirst==True:
                end=mid-1
             else:
              start=mid+1
         elif x<A[mid]:
            end=mid-1
         else:
             start=mid+1
    return result

        
print(binary([1,2,3,4,5,6,7,8,9,10,10,10,15],10,True))

#t looks like you are using Python 3.x. One of the important differences in Python 3.x is the way division is handled. When you do x / y, an integer is returned in Python 2.x because the decimal is truncated (floor division). However in 3.x, the / operator performs 'true' division, resulting in a float instead of an integer (e.g. 1 / 2 = 0.5). What this means is that your are now trying to use a float to reference a position in a list (e.g. my_list[0.5] or even my_list[1.0]), which will not work as Python is expecting an integer. Therefore you may first want to try using middle = (first + last) // 2, adjusting so that the result returns what you expect.
#The // indicates floor division in Python 3.x.

