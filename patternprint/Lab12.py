'''
1
12
123
1234
12345
123456
1234567
12345678
123456789
12345678910
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
