'''
    4
   3 4
  2 3 4
 1 2 3 4
0 1 2 3 4
 1 2 3 4
  2 3 4
   3 4
    4 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(0,i):
        print(num+j-i,end=" ")
    print()
for k in range(1,num):
    print(" "*k,end="")
    for l in range(1,num+1-k):
        print(l+k-1,end=" ")
    print()