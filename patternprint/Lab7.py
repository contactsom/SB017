'''
10987654321
10987654321
10987654321
10987654321
10987654321
10987654321
10987654321
10987654321
10987654321
10987654321
'''

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-j,end=" ")
    print()
