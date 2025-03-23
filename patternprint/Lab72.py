'''
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(1,num+2-i):
        print(num-i+1,end=" ")
    print()