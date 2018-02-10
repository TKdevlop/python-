lis=[5,20,5,4,100]
#range is one most common genrater
#list comprehension store this in this store in the memory
#list comprehension is faster as they stored in memory in ram
#generator is gonna be slower but they are not gonna store in memory
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
for i in xyz:  #we cannot print xyz as it is genrater therefore we use i to print
    #xyz content
    print(i)
    
[print(e) for e in range(5)]


# when sometime to build a list and save to it the varible then genrater are faster
# then list


#example

# xyz=[i for i in range(10)] # list comprehension output: 0,1,2,3,4



#xyz=(i for i in range(10)) # generator expressing output : genarator object

 #the only diffrence between genrater and list is parenthes




xyz=[[(i,ii)for ii in range(5)]for i in range(5)]
print(xyz)# rather than the colon
# you have bracket bomm boom

for i in range(5):
    for ii in range(5):
        print(i,ii)


xyz=(((i,ii)for ii in range(5))for i in range(5))# output is gerater object
# if print xyz 
#print([i for i in xyz]) # one line statement for printing xyz
for i in xyz:
    for ii in i:  # we only itrate  i as its itrate inner loop(ii) itself
     print(ii) # give us that desire output


     # in list compresion you run out memory if big thing occur but 
     # in  big generators you run out time
     xyz=(print(i) for i in range(5))# no output
     for i in xyz:
         i# we just need to write i as print already done in 

     























