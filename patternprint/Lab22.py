'''
JJJJJJJJJJ
IIIIIIIII
HHHHHHHH
GGGGGGG
FFFFFF
EEEEE
DDDD
CCC
BB
A
'''

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(65+n-i),end=" ")
    print()