'''
          A
        A B C
       A B C D E
      A B C D E F G
     A B C D E F G H I
    A B C D E F G H I J K
   A B C D E F G H I J K L M
  A B C D E F G H I J K L M N O
 A B C D E F G H I J K L M N O P Q
A B C D E F G H I J K L M N O P Q R S
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(65,65+2*i-1):
        print(chr(j), end=" ")
    print()