##x=int(input("Enter any number"))
##
##i = x-1 + x-2
##
##print(i)
a=[]
def f(n):
     if n==0 or n==1:
         return 1
     if a[n] != -1:
          return a[n]
     else a[n]= f(n-1)+ f(n-2):
          return a[n]

def main():
     for i in range(100):
          a[i]=-1
print(f(6))
