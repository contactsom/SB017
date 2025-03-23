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
    for j in range(1,i+1):
        print(num-i+j-1,end=" ")
    print()
for a in range(1,num+1):
    for k in range(0,num-a):
        print(k+a,end=" ")
    print()