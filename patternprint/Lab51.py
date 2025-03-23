'''
1 2 3 4 5 6 7 8 9
 1 2 3 4 5 6 7
  1 2 3 4 5
   1 2 3
    1 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(1,num+2-i):
        print(j,end=" ")
    for k in range(2,num+2-i):
        print(num+k-i,end=" ")
    print()