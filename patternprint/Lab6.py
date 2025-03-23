'''
10101010101010101010
9999999999
8888888888
7777777777
6666666666
5555555555
4444444444
3333333333
2222222222
1111111111
'''

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=" ")
    print()