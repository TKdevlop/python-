def fun(a,b,c):
    print(a+b)
    c()
    z="{}{}".format(c())
    print(z)



fun(5,5, c=lambda  :print("hello") )
