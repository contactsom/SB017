'''
AAAAAAAAAA
BBBBBBBBB
CCCCCCCC
DDDDDDD
EEEEEE
FFFFF
GGGG
HHH
II
J
'''

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+i),end=" ")
    print()