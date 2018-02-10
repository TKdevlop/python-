arr=(2,4,5)
##
##for c1 in range(10):
##    for c2 in range(10):
##        for c3 in range(10):
##            if (c1,c2,c3) == arr:
##                print("found the combo: {}".format((c1,c2,c3)))
##                break
##            print(c1,c2,c3)
            
##string formating                
##for (c1,c2,c3) in arr:
##    if(c1,c2,c3)==arr:
##        print(c1,c2,c3)
            
def comgen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                
                yield(c1,c2,c3)# you can use genrater anything you want
                

for (c1,c2,c3) in comgen():
    print(c1,c2,c3)
    if (c1,c2,c3)==arr:
        print("found the combo: {}".format((c1,c2,c3)))
        break
