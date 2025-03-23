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
    for j in range(1,i+1):
        print(num-j,end=" ")
    print()
for a in range(1,num+1):
    for k in range(1,num+1-a):
        print(num - k, end=" ")
    print()