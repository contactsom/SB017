'''
10987654321
1098765432
109876543
10987654
1098765
109876
10987
1098
109
10
'''

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-j,end=" ")
    print()