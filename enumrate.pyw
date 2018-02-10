example=["left","right","up","down"]

for i in range(len(example)):
    
    print(i,example[i])


for i,j in enumerate(example): # enumerate is  a funtion used to do what its say
    print(i,j)
               

new=dict(enumerate(example))
print(new)
         


#zip funtion
x=[1,2,3,4]
y=[5,6,7,8]
z=["a","b","c"]

#for x,y,z in zip(x,y,z):
#    print(x,y,z )
##for i in zip(x,y,z): # its funtion is to combine the list
##    print(list(zip())) # zip is an object and can be itrated over and over
##    print(i) # we can also print as a list

di=dict(zip(x,y))
print(di)
