'''
    1
   2 2
  3   3
 4     4
5       5
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(i,i+1):
        print(i,end=" ")
    if i>=2:
        print(" "*(2*i-4),end="")
        for k in range(i,i+1):
            print(i,end=" ")
    print()