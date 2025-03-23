'''
     A
   A B A
  A B C A B
 A B C D A B C
A B C D E A B C D
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    for k in range(1,i):
        print(chr(64+k),end=" ")
    print()