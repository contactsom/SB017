'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
'''

num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for k in range(1, num):
    print(" "*k,end="")
    for l in range(1,num+1-k):
        print(l,end=" ")
    print()
