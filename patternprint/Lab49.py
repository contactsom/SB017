'''
5 5 5 5 5 5 5 5 5
 4 4 4 4 4 4 4
  3 3 3 3 3
   2 2 2
    1 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(0,num+1-i):
        print(num+1-i,end=" ")
    for k in range(1,num+1-i):
        print(num+1-i,end=" ")
    print()