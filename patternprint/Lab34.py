'''
A B C D E F G H I J
 A B C D E F G H I
  A B C D E F G H
   A B C D E F G
    A B C D E F
     A B C D E
      A B C D
       A B C
        A B
         A 
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(65,66+n-i):
        print(chr(j),end=" ")
    print()