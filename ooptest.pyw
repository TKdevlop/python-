class stone:
    numberofstone=0
    colletion=[]
    def __init__(self,name):
        self.name=name
        stone.numberofstone+=1
        
        if stone.numberofstone <=5:
            stone.colletion.append(self)
        else:
            del stone.colletion[0]
            stone.colletion.append(self)


    @staticmethod
    def showthat():
           for stone in stone.colletion:
               print(stone.colletion,end=" ")
             
            
                

stoneone=stone("ruby")
print(stoneone.name)
stonetwo=stone("emerald")
print(stonetwo.name)
stonetwo.showthat()
        
##
##    def test(self):
##        self.st="test"
####    def pre(self,st):
####         if st > 4:
##            return "your cannot stor any more stone"
##         else:
##            return "stone are stored"
##
##
##precious=stone()
##precious.st
###print(precious.st)
        
