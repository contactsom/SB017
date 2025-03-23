'''
12345678910
123456789
12345678
1234567
123456
12345
1234
123
12
1
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=" ")
    print()