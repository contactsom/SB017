# How to declare the Function

a = 100 # Global

def m1():
    a = 10 # Local Variable
    print(globals()['a'])

def m2():
    print(a)

def m3():
    print(a)

def m4():
    print(a)

#CALL
m1()
m2()
m3()
m4()