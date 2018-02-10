def match(string1,string2):
    for i in string1:
        for j in string2:
            if string1[i]==string2[j]:
                print(i)
                return True
            else:
                return False
            
            
            
print(match("aa","a"))            
            
            
            
