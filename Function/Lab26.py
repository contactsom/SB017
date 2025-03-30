# How to declare the Function


a =100
def m1():
    a = 10
    def m2():
        a=1
        print ("in m2: ",a) #1
    m2() #1
    print ("in m1",a)

m1()