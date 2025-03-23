'''
10101010101010101010
999999999
88888888
7777777
666666
55555
4444
333
22
1
'''

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-i,end=" ")
    print()