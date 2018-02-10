def re(x,y):
	if y==0:
		return 1
	else:
		return x *re(x,y-1)
	    

print(re(2,3))
	    
