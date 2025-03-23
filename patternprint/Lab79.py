'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 2 3 4 5
  3 4 5
   4 5
    5 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for p in range(1,num):
    print(" " * p, end="")
    for q in range(1, num + 1 - p):
        print(q + p, end=" ")
    print()