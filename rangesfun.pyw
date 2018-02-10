lis=[5,20,5,4,100]

def div5(x):
    if x%5==0:
        return True
    else:
        return False
    
xyz=(i for i in lis if div5(i))# use same logic as down in one line

#xyz=[]
#for i in lis:
 #   if div5(i):
  #      xyz.append(i)
for i in xyz:
    print(i)
    
[print(e) for e in range(5)]


