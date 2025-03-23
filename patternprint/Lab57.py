'''
    4
   4 3
  4 3 2
 4 3 2 1
4 3 2 1 0
 4 3 2 1
  4 3 2
   4 3
    4
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print(num - j, end=" ")
    print()
for k in range(1, num):
    print(" " * k, end="")
    for l in range(1, num + 1 - k):
        print(num - l, end=" ")
    print()