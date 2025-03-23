'''
JIHGFEDCBA
JIHGFEDCB
JIHGFEDC
JIHGFED
JIHGFE
JIHGF
JIHG
JIH
JI
J
'''

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(65+n-j),end=" ")
    print()