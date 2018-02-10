class ey():
    hours=10
    @staticmethod #static method that did not take self paprameter decoraters are funtion that extents another funtions and extent there funtionality 
    def mms(): # there are deonated by starting by @ symbol
        print("Hellow world")


rahul=ey()
tushar=ey()
tushar.hours=20
print(tushar.hours)
tushar.name="tushar kahrbanda"# attribute is created only for only for tushar
print(tushar.name)#both of these are instance attribute that are assecible to that particular object
rahul.name="rahul kharbanda"
print(rahul.name)

tushar.mms()
