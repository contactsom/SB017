'''
1       1
 2     2
  3   3
   4 4
    5 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(i,i+1):
        print(i,end=" ")
    if i<num:
        print(" "*(2*num-2*i-2),end="")
        for k in range(i,i+1):
            print(i,end=" ")
    print()