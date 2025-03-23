'''
    5
   4 4
  3   3
 2     2
1       1

'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(i,i+1):
        print(num+1-i, end=" ")
    if i >= 2:
        print(" " * (2 * i - 4), end="")
        for k in range(i, i + 1):
            print(num + 1-i, end=" ")
    print()