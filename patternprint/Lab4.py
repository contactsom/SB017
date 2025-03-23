'''
AAAAAAAAAA
BBBBBBBBBB
CCCCCCCCCC
DDDDDDDDDD
EEEEEEEEEE
FFFFFFFFFF
GGGGGGGGGG
HHHHHHHHHH
IIIIIIIIII
JJJJJJJJJJ
'''

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()
