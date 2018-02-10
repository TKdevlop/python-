import timeit  # time moudule use for calculating the time between operation

#print(timeit.timeit("1+3", number=50000000))#number stand for how many time we need to do task


input_list=range(100)
def div5(num):
    if num%5==0:
       return True
    else:
        return False
    
    
xyz=(i for i in input_list if div5(i))    

xyz=[i for i in input_list if div5(i)]

print(timeit.timeit("""

input_list=range(100)
def div5(num):
    if num%5==0:
       return True
    else:
       return False
xyz=list((i for i in input_list if div5(i)))"""
                ,number=5000))#you cannot run only xyz as timeit doen't have acess to above come
#xyz=[i for i in input_list if div5(i)]  #spedd = 0.0978 for list
#speed= 0.00377  for ganarator

input_list=range(100)
def div5(num):
    if num%5==0:
       return True
    else:
       return False
xyz=list((i for i in input_list if div5(i)))

for i in xyz:
    print(i)
