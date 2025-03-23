'''
1111111111
222222222
33333333
4444444
555555
66666
7777
888
99
10
'''

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(i,end=" ")
    print()