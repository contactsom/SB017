'''
5 4 3 2 1
 4 3 2 1
  3 2 1
   2 1
    1 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(1,num+2-i):
        print(num+2-i-j,end=" ")
    print()