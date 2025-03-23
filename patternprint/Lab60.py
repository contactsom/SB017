'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for a in range(1,num+1):
    for k in range(1,num+1-a):
        print("*",end=" ")
    print()